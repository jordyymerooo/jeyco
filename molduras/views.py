from django.shortcuts import render
from .models import Moldings
from .models import Molduras

def moldura(request):
    molduras = Molduras.objects.all()
    return render(request, 'moldura.html',{'molduras':molduras})


def molding(request):
    molduras = Moldings.objects.all()
    return render(request, 'moldings.html',{'molding':molding})


