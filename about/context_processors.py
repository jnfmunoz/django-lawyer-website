from .models import About

def about(request, *args, **kwargs):
    about = About.objects.all()

    context = {
        'about': about,
    }

    return context