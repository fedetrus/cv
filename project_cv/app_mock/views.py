# app_mock/views.py
from django.views.generic import ListView
from .models import Technology, Project, Trabajo, Academia

class TechnologyListView(ListView):
    model = Technology
    template_name = 'app_mock/main.html' 
    context_object_name = 'technologies' 

    def get_queryset(self):
        return Technology.objects.filter(status=True).order_by('nro_orden')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intro_logo'] = Technology.objects.filter(name="django").first()
        context['projects'] = Project.objects.filter(status=True).prefetch_related('technologies', 'images').order_by('nro_orden')
        context['trabajos'] = Trabajo.objects.all().prefetch_related('puestos')
        context['academias'] = Academia.objects.all().prefetch_related('carreras')
        return context

import subprocess
from django.http import HttpResponse
import os
import tempfile
from datetime import datetime

def generate_pdf(request):
    """Genera un PDF capturando la página en modo oscuro o claro según la versión elegida."""

    url = request.build_absolute_uri('/')  # URL actual
    is_light = request.GET.get("light", "false").lower() == "true"  # Detectar si es versión light
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name  # Archivo temporal

    # Obtener la fecha actual en formato dd-mm-yyyy
    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    version = "Light" if is_light else "Dark"
    pdf_filename = f"CV_Federico-Suarez_{version}_{fecha_actual}.pdf"

    # Construir el script de Pyppeteer dinámicamente
    script = f"""
        import asyncio
        from pyppeteer import launch

        async def main():
            browser = await launch(headless=True, args=['--no-sandbox', '--disable-gpu'])
            page = await browser.newPage()
            await page.goto('{url}', {{'waitUntil': 'networkidle2'}})  # Espera que cargue todo

            # Si el usuario eligió la versión Light, cambiar el tema a Light
            { "await page.evaluate('document.documentElement.setAttribute(\"data-theme\", \"light\")')" if is_light else "" }

            # Obtener la altura exacta del contenido sin generar espacio extra
            body_height = await page.evaluate('Math.min(document.body.scrollHeight, 4500)')

            # Generar el PDF con altura dinámica ajustada
            await page.pdf(path="{pdf_path}", width="1920px", height=f"{{body_height}}px", printBackground=True)
            
            await browser.close()

        asyncio.run(main())
        """
    # Ejecutar Pyppeteer en un subproceso separado
    subprocess.run(["python3", "-c", script], check=True)

    # Leer el archivo PDF generado y devolverlo como respuesta
    with open(pdf_path, "rb") as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'

    # Eliminar el archivo temporal
    os.remove(pdf_path)

    return response
