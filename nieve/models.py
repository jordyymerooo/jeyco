from django.db import models

class Snow(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='nieve/images', null=True, blank=True)
    video = models.FileField(upload_to='nieve/video/%Y', null=True, blank=True)

class Nieve(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='nieve/images', null=True, blank=True)
    video = models.FileField(upload_to='nieve/video/%Y', null=True, blank=True)
