from .models import Feature

def feature(request, *args, **kwargs):
    features = Feature.objects.all()
    counter = [f"{i:02}" for i in range(1, len(features) + 1)]

    features_with_counter = zip(counter, features)
    context = {
        'features': features_with_counter,
    }

    return context
