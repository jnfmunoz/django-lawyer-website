from django.shortcuts import render

# Create your views here.
def attorneys_view(request, *args, **kwargs):
    return render(request, 'attorneys.html', context={})
