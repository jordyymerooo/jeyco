from django.db import models

class Carpentry(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='carpinteria/images', null=True, blank=True)
    video = models.FileField(upload_to='carpinteria/video/%Y', null=True, blank=True)

class Carpinterias(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='carpinteria/images', null=True, blank=True)
    video = models.FileField(upload_to='carpinteria/video/%Y', null=True, blank=True)
