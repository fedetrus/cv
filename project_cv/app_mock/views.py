# app_mock/views.py
from django.views.generic import ListView
from .models import Technology, Project, Trabajo

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
        return context
