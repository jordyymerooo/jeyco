from django.shortcuts import render
from .models import Snow
from .models import Nieve

def nieve(request):
    nieves = Nieve.objects.all()
    return render(request, 'nieve.html',{'nieves':nieves})

def snow(request):
    snows = Snow.objects.all()
    return render(request, 'snow.html',{'snows':snows})

