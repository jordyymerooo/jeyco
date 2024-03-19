from django.shortcuts import render
from .models import Decks
from .models import Cubiertas

def cubierta(request):
    cubiertas = Cubiertas.objects.all()
    return render(request, 'cubiertas.html',{'cubiertas':cubiertas})


def deck(request):
    decks = Decks.objects.all()
    return render(request, 'decks.html',{'decks':decks})
