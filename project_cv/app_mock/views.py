from django.views.generic import ListView
from .models import Technology

class TechnologyListView(ListView):
    model = Technology
    template_name = 'app_mock/main.html'  # Nombre del template
    context_object_name = 'technologies'  # Cómo se llamará el queryset en tu template

