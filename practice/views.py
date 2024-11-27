from django.shortcuts import render
from .models import PracticeArea

# Create your views here.
def practice_view(request, *args, **kwargs):
    practice_areas = PracticeArea.objects.all()
   
    context={
        'practice_areas':practice_areas
    }

    return render(request, 'practice.html', context)
