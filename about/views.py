from django.shortcuts import render
from features.models import Feature

# Create your views here.
def about_view(request, *args, **kwargs):
    return render(request, 'about.html')