# CS350-Project-1/play/urls.py

from django.urls import path
from .views import PlayView, PlayAverageView

urlpatterns = [
    path('<int:num_cards>/<int:round>/<int:index>/<str:shuffle>/<int:bpk>/<str:wpks>/', PlayView.as_view(), name='play-view'),
    path('score/<int:num_cards>/<int:round>/<int:index>/<str:shuffle>/<int:bpk>/<str:wpks>/', PlayAverageView.as_view(), name='play-score-view')
]
