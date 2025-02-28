
import subprocess
from django.http import HttpResponse
import tempfile
from datetime import datetime

def generate_pdf(request):
    """Genera un PDF desde HTML con WKHTMLTOPDF respetando el tema Dark o Light"""

    url = request.build_absolute_uri('/')

    # Detectar si el usuario quiere la versión Light
    is_light = request.GET.get("light", "false").lower() == "true"

    # Script que forzará el cambio de tema antes de la conversión
    js_script = ""
    if is_light:
        js_script = "document.documentElement.setAttribute('data-theme', 'light');"
    else:
        js_script = "document.documentElement.setAttribute('data-theme', 'dark');"
        
    # Nombre del archivo PDF con fecha
    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    version = "Light" if is_light else "Dark"
    pdf_filename = f"CV_Federico-Suarez_{version}_{fecha_actual}.pdf"

    # Crear un archivo temporal para el PDF
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

    # Ejecutar wkhtmltopdf con JS para forzar el tema Light si corresponde
    command = [
        "wkhtmltopdf",
        "--page-width", "1800px",
        "--page-height", "3500px",
        "--enable-javascript",
        "--javascript-delay", "1500",  # Tiempo de espera para que Bulma aplique los estilos
        "--run-script", js_script,
        url,
        pdf_path
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        return HttpResponse(f"Error al generar PDF: {result.stderr}", status=500)

    # Leer el PDF generado
    with open(pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()

    response = HttpResponse(pdf_content, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'

    return response
