from django.shortcuts import render
from .models import Demolition
from .models import Demolicion

def demolicion(request):
    demolicions = Demolicion.objects.all()
    return render(request, 'demolicion.html',{'demolicions':demolicions})

def demolition(request):
    demolitions = Demolition.objects.all()
    return render(request, 'demolition.html',{'demolicions':demolitions})

