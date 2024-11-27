from django.shortcuts import render
from features.models import Feature
from .models import About

# Create your views here.
def about_view(request, *args, **kwargs):
    features = Feature.objects.all()
    counter = [f"{i:02}" for i in range(1, len(features) + 1)]
    about = About.objects.all()

    features_with_counter = zip(counter, features)

    context = {
        'about':about,
        'features_with_counter':features_with_counter,
    }

    return render(request, 'about.html', context)