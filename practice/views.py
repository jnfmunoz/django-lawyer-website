from django.shortcuts import render
from .models import PracticeArea

# Create your views here.
def practice_view(request, *args, **kwargs):
    return render(request, 'practice.html')

