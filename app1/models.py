from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=40)
    dni = models.IntegerField()
    nacdate = models.CharField(max_length=15)


