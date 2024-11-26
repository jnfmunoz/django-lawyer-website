from django.shortcuts import render

# Create your views here.
def about_view(request, *args, **kwargs):
    return render(request, 'about.html', context={})