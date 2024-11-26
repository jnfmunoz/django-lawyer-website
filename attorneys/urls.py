from django.urls import path
from . import views

urlpatterns = [
    path('', views.attorneys_view, name='attorneys'),
]