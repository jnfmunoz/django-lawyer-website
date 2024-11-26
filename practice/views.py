from django.shortcuts import render

# Create your views here.
def practice_view(request, *args, **kwargs):
    return render(request, 'practice.html', context={})
