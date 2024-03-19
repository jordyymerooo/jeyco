from django.db import models

class Doorswindows(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='puertaventana/images', null=True, blank=True)
    video = models.FileField(upload_to='puertaventana/video/%Y', null=True, blank=True)

class Puertaventanas(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='puertaventana/images', null=True, blank=True)
    video = models.FileField(upload_to='puertaventana/video/%Y', null=True, blank=True)

