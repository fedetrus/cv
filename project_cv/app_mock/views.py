# app_mock/views.py
from django.views.generic import ListView
from .models import Technology, Project

class TechnologyListView(ListView):
    model = Technology
    template_name = 'app_mock/main.html' 
    context_object_name = 'technologies' 

    def get_queryset(self):
        return Technology.objects.filter(status=True).order_by('nro_orden')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intro_logo'] = Technology.objects.filter(name="Django").first()  # Obtiene solo Django
        context['projects'] = Project.objects.filter(status=True).order_by('nro_orden')  # Obtiene los proyectos activos y ordenados
        return context
