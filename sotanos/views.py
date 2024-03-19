from django.shortcuts import render
from .models import Basement
from .models import Sotanos

def sotano(request):
    sotanos = Sotanos.objects.all()
    return render(request, 'sotano.html',{'sotanos':sotanos})


def basement(request):
    basements = Basement.objects.all()
    return render(request, 'basement.html',{'basements':basements})


