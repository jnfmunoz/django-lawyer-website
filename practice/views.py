from django.shortcuts import render
from .models import PracticeArea

# Create your views here.
def practice_view(request, *args, **kwargs):
    practice_areas = PracticeArea.objects.all()

    # Crear una lista de diccionarios con los valores originales y el calculado
    practice_areas_with_icons = []
    for area in practice_areas:
        formatted_icon_value = area.get_formatted_icon()
        # print(formatted_icon_value)
        practice_areas_with_icons.append({
            'title': area.title,
            'description': area.description,
            'formatted_icon': formatted_icon_value
        })

    context = {
        'practice_areas': practice_areas_with_icons
    }

    # print(context)  # verificar los valores
    return render(request, 'practice.html', context)

