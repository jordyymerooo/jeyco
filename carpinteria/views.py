from django.shortcuts import render
from .models import Carpentry
from .models import Carpinterias

def carpinteria(request):
    carpinterias = Carpinterias.objects.all()
    return render(request, 'carpinteria.html',{'carpinterias':carpinterias})


def carpentry(request):
    carpentrys = Carpentry.objects.all()
    return render(request, 'carpentry.html',{'carpentrys':carpentrys})
