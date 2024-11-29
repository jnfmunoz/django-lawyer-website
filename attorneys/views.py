from django.shortcuts import render
from .models import Attorney
from features.models import Feature


# Create your views here.
def attorneys_view(request, *args, **kwargs):
    attorneys = Attorney.objects.all()
    features = Feature.objects.all()
    counter = [f"{i:02}" for i in range(1, len(features) + 1)]

    features_with_counter = zip(counter, features)

    context = {
        'attorneys':attorneys,
        'features_with_counter':features_with_counter,
    }

    return render(request, 'attorneys.html', context)