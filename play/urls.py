# CS350-Project-1/play/urls.py

from django.urls import path
from .views import PlayView, PlayAverageView

urlpatterns = [
    path('<int:round>/<str:shuffle>/<int:bpk>/<str:wpks>', PlayView.as_view(), name='play-view'),
    path('average/<int:round>/<str:shuffle>/<int:bpk>/<str:wpks>', PlayAverageView.as_view(), name='play-view'),
]
