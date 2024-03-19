from django.db import models

class Decks(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='cubierta/images', null=True, blank=True)
    video = models.FileField(upload_to='cubierta/video/%Y', null=True, blank=True)

class Cubiertas(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='cubierta/images', null=True, blank=True)
    video = models.FileField(upload_to='cubierta/video/%Y', null=True, blank=True)


