from django.db import models

class Moldings(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='moldura/images', null=True, blank=True)
    video = models.FileField(upload_to='moldura/video/%Y', null=True, blank=True)

class Molduras(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='moldura/images', null=True, blank=True)
    video = models.FileField(upload_to='moldura/video/%Y', null=True, blank=True)
