from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='blog/images', null=True, blank=True) 
    video = models.FileField(upload_to='blog/video/%Y', null=True, blank=True)
    

