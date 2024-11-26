from django.shortcuts import render
from features.models import Feature

def index(request, *args, **kwargs):
    features = Feature.objects.all()

    return render(request, 'index.html', context={'features':features})