# app_mock/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import TechnologyListView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='app_mock/base.html'), name='base'),
    path('', TechnologyListView.as_view(), name='main'),
]
