from django.shortcuts import render
from features.models import Feature

# Create your views here.
def about_view(request, *args, **kwargs):
    features = Feature.objects.all()

    return render(request, 'about.html', context={'features':features})