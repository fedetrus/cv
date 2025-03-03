import subprocess
from django.http import HttpResponse
import os
import tempfile
from datetime import datetime

def generate_pdf(request):
    url = request.build_absolute_uri('/')
    is_light = request.GET.get("light", "false").lower() == "true"
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    pdf_filename = f"CV_Federico-Suarez_{fecha_actual}.pdf"

    script = f"""
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(
        headless=True,
        args=[
            '--no-sandbox',
            '--disable-gpu',
            '--single-process',
            '--disable-dev-shm-usage',
            '--disable-web-security'
        ]
    )
    page = await browser.newPage()

    # Agregar User-Agent para evitar bloqueos
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    await page.goto('{url}', {{'waitUntil': 'networkidle2'}})

    # Si el usuario eligió la versión Light, cambiar el tema
    if {is_light}:
        await page.evaluate('document.documentElement.setAttribute("data-theme", "light")')

    # Ocultar el navbar solo en la impresión
    await page.evaluate('document.getElementById("nav-no-print").style.display = "none";')

    # Esperar un poco más para asegurarse de que todo cargó
    await asyncio.sleep(3)


    # Generar el PDF con la altura real del contenido
    await page.pdf(
        path="{pdf_path}",
        width="1920px",
        height="4400px",  # Se ajusta dinámicamente
        printBackground=True
    )

    await browser.close()

asyncio.run(main())
"""

    # Ejecutar Pyppeteer en subproceso y capturar salida
    result = subprocess.run(["python3", "-c", script], capture_output=True, text=True)

    # Guardar errores en un archivo temporal para revisarlos
    error_log_path = "/tmp/pyppeteer_error.log"
    with open(error_log_path, "w") as error_log:
        error_log.write(f"RETURNCODE: {result.returncode}\n")
        error_log.write(f"STDOUT:\n{result.stdout}\n")
        error_log.write(f"STDERR:\n{result.stderr}\n")

    if result.returncode != 0:
        raise subprocess.CalledProcessError(
            result.returncode, result.args,
            output=result.stdout, stderr=result.stderr
        )

    with open(pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()

    response = HttpResponse(pdf_content, content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
    os.remove(pdf_path)

    return response
