from django.shortcuts import render
from .models import Doorswindows
from .models import Puertaventanas

def puertaventana(request):
    puertaventanas = Puertaventanas.objects.all()
    return render(request, 'puertaventana.html',{'puertaventanas':puertaventanas})


def doorswindow(request):
    doorswindows = Doorswindows.objects.all()
    return render(request, 'doorswindows.html',{'doorswindows':doorswindows})
