import subprocess
from django.http import HttpResponse
import tempfile
from datetime import datetime

def generate_pdf(request):
    """Genera un PDF desde HTML con WKHTMLTOPDF"""

    # Obtener la URL de la página actual
    url = request.build_absolute_uri('/')

    # Detectar si el usuario quiere la versión Light
    is_light = request.GET.get("light", "false").lower() == "true"

    # Agregar parámetro en la URL para activar el modo claro
    if is_light:
        url += "?theme=light"

    # Nombre del archivo PDF con fecha
    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    version = "Light" if is_light else "Dark"
    pdf_filename = f"CV_Federico-Suarez_{version}_{fecha_actual}.pdf"

    # Crear un archivo temporal para el PDF
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

    # Ejecutar wkhtmltopdf
    result = subprocess.run(
        ["wkhtmltopdf", "--page-width", "1920px", "--page-height", "99999px", url, pdf_path],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        return HttpResponse(f"Error al generar PDF: {result.stderr}", status=500)

    # Leer el PDF generado
    with open(pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()

    response = HttpResponse(pdf_content, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'

    return response
