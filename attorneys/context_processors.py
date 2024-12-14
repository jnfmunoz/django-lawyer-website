from .models import Attorney

def attorney(request, *args, **kwargs):
    attorneys = Attorney.objects.all()

    context = {
        'attorneys':attorneys,
    }

    return context