from django.db import models

class Project(models.Model):
    image=  models.ImageField(upload_to='portfolio/images')
class Proyecto(models.Model):
    image=  models.ImageField(upload_to='portfolio/images')

