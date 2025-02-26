# app_mock/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import TechnologyListView, generate_pdf

urlpatterns = [
    path('', TechnologyListView.as_view(), name='main'),
    path('descargar-pdf/', generate_pdf, name='descargar_pdf'),
]
