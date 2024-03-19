from django.db import models

class Basement(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='sotano/images', null=True, blank=True)
    video = models.FileField(upload_to='sotano/video/%Y', null=True, blank=True)

class Sotanos(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='sotano/images', null=True, blank=True)
    video = models.FileField(upload_to='sotano/video/%Y', null=True, blank=True)
