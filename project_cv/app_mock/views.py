# app_mock/views.py
from django.views.generic import ListView
from .models import Technology

class TechnologyListView(ListView):
    model = Technology
    template_name = 'app_mock/main.html' 
    context_object_name = 'technologies' 

    def get_queryset(self):
        return Technology.objects.filter(status=True).order_by('nro_orden')

