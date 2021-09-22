# CS350-Project-1/start/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

class StartTemplateView(TemplateView):
    template_name = 'index.html'
