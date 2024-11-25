from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, 'index.html', context={})

def about(request, *args, **kwargs):
    return render(request, 'about.html', context={})