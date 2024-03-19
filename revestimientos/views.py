from django.shortcuts import render
from .models import Revestimientos
from .models import Siding

def revestimiento(request):
    revestimientos = Revestimientos.objects.all()
    return render(request, 'revestimiento.html',{'revestimientos':revestimientos})

def siding(request):
    sidings = Siding.objects.all()
    return render(request, 'siding.html',{'sidings':sidings})
