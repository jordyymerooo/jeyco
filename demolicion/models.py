from django.db import models

class Demolicion(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='demolicion/images', null=True, blank=True)
    video = models.FileField(upload_to='demolicion/video/%Y', null=True, blank=True)
class Demolition(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='demolicion/images', null=True, blank=True)
    video = models.FileField(upload_to='demolicion/video/%Y', null=True, blank=True)