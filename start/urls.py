# CS350-Project-1/start/urls.py

from django.urls import path
from .views import StartTemplateView

urlpatterns = [
    path('', StartTemplateView.as_view(), name='index-view'),
]