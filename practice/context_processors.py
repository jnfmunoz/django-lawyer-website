from .models import PracticeArea

def practice_area(request, *args, **kwargs):
    practice_areas = PracticeArea.objects.all()

    # Crear una lista con los valores formatedos
    formatted_practice_areas = []
    for area in practice_areas:
        formatted_icon_value = area.get_practice_formatted_icon()
        formatted_practice_areas.append({
            'title': area.title,
            'description': area.description,
            'formatted_icon': formatted_icon_value
        })
    # print(formatted_practice_areas)

    context = {
        'practice_areas': formatted_practice_areas
    }

    return context