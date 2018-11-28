from django.shortcuts import render
from .models import CarPost

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})

def post(request):
    context = {
    'cars': CarPost.objects.all()
    }
    return render(request, 'blog/cars.html', context)
