# CS350-Project-1/end/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

class EndTemplateView(TemplateView):
    template_name = 'end.html'
