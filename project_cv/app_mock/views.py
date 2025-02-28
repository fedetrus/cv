# app_mock/views.py
from django.views.generic import ListView
from .models import Technology, Project, Trabajo, Academia, Carrera
from django.db.models import Prefetch


class TechnologyListView(ListView):
    model = Technology
    template_name = 'app_mock/main.html' 
    context_object_name = 'technologies' 

    def get_queryset(self):
        return Technology.objects.filter(status=True).order_by('nro_orden')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Convertir rutas relativas de las imágenes en absolutas
        for tech in context["technologies"]:
            if tech.logo:  # Evita errores si no tiene imagen
                tech.absolute_logo_url = self.request.build_absolute_uri(tech.logo.url)

        context['intro_logo'] = Technology.objects.filter(name="django").first()
        if context['intro_logo'] and context['intro_logo'].logo:
            context['intro_logo'].absolute_logo_url = self.request.build_absolute_uri(context['intro_logo'].logo.url)
            
        context['projects'] = Project.objects.filter(status=True).prefetch_related('technologies', 'images').order_by('nro_orden')
        context['trabajos'] = Trabajo.objects.all().prefetch_related('puestos')
        context['academias'] = Academia.objects.prefetch_related(
            Prefetch('carreras', queryset=Carrera.objects.filter(status=True))
        )
        
        return context
