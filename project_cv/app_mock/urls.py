# app_mock/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import TechnologyListView

urlpatterns = [
    path('', TechnologyListView.as_view(), name='main'),
]
