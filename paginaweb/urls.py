"""
URL configuration for paginaweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from portfolio import views as portfolio_views
from blog import views as blog_views
from django.conf.urls.static import static
from cubiertas import views as cubiertas_views
from puertaventana import views as puertaventanas_views
from molduras import views as molduras_views
from sotanos import views as  sotano_views
from carpinteria import views as  carpinteria_views
from demolicion import views as  demolicion_views
from nieve import views as  nieve_views
from revestimientos import views as  revestimiento_views






urlpatterns = [
    path('admin/', admin.site.urls),
    path('',portfolio_views.home, name='home'),
    path('portfolio/',portfolio_views.hogar, name='hogar'),
    path('contact/', portfolio_views.contact, name='contact'),
    path('deck/',cubiertas_views.deck, name='deck' ),
    path('cubiertas/',cubiertas_views.cubierta, name='cubierta' ),
    path('doorswindow/',puertaventanas_views.doorswindow, name='doorswindow' ),
    path('puertaventana/',puertaventanas_views.puertaventana, name='puertaventana' ),
    path('molding/',molduras_views.molding, name='molding' ),
    path('molduras/',molduras_views.moldura, name='moldura' ),
    path('capentry/',carpinteria_views.carpentry, name='carpentry' ),
    path('capinteria/',carpinteria_views.carpinteria, name='carpinteria' ),
    path('demolition/',demolicion_views.demolition, name='demolition' ),
    path('demolicion/',demolicion_views.demolicion, name='demolicion' ),
    path('snow/',nieve_views.snow, name='snow' ),
    path('nieve/',nieve_views.nieve, name='nieve' ),
    path('basement/',sotano_views.basement, name='basement' ),
    path('sotanos/',sotano_views.sotano, name='sotano' ),
    path('revestimiento/',revestimiento_views.revestimiento, name='revestimiento' ),
    path('siding/',revestimiento_views.siding, name='siding' ),
    path('blog/', blog_views.render_publicacion, name='publicacion'),
    path('blog/posts/', blog_views.render_posts, name='posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

