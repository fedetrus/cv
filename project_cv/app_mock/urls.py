# app_mock/urls.py
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='app_mock/base.html'), name='base'),
]
