# CS350-Project-1/play/urls.py

from django.urls import path
from .views import PlayTemplateView

urlpatterns = [
    path('', PlayTemplateView.as_view(), name='play-view'),
]
