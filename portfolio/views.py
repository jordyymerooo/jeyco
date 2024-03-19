from django.shortcuts import render, redirect
from .models import Project
from .models import Proyecto
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def hogar(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'hogar.html', {'proyectos': proyectos})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['jordanymb7@gmail.com']
        )

        email.send(fail_silently=False)

        messages.success(request, 'Se ha enviado tu correo.')
        return redirect('home')
    return render(request, 'home.html')
