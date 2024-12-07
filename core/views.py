from django.shortcuts import render
from features.models import Feature
from about.models import About
from attorneys.models import Attorney
from practice.models import PracticeArea

def index(request, *args, **kwargs):
    features = Feature.objects.all()
    counter = [f"{i:02}" for i in range(1, len(features) + 1)]
    about = About.objects.all()
    attorneys = Attorney.objects.all()
    practice_areas = PracticeArea.objects.all()

    features_with_counter = zip(counter, features)

    # Crear una lista de diccionarios con los valores originales y el calculado
    practice_areas_with_icons = []
    for area in practice_areas:
        formatted_icon_value = area.formated_icon()
        practice_areas_with_icons.append({
            'title': area.title,
            'description': area.description,
            'formatted_icon': formatted_icon_value
        })

    context = {
        'about':about,
        'features_with_counter':features_with_counter,
        'attorneys':attorneys,
        'practice_areas': practice_areas_with_icons,
    }

    return render(request, 'index.html', context)