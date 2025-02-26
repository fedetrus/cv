# app_mock/urls.py
from django.urls import path
from .views import TechnologyListView
from .utils import generate_pdf

urlpatterns = [
    path('', TechnologyListView.as_view(), name='main'),
    path('descargar-pdf/', generate_pdf, name='descargar_pdf'),
]
