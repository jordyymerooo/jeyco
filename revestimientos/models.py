from django.db import models

class Revestimientos(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='revestimiento/images', null=True, blank=True)
    video = models.FileField(upload_to='revestimiento/video/%Y', null=True, blank=True)
class Siding(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='revestimiento/images', null=True, blank=True)
    video = models.FileField(upload_to='revestimiento/video/%Y', null=True, blank=True)
