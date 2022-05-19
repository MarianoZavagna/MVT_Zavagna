from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=40)
    dni = models.IntegerField()
    # agregar nacdate = models.DateField()  ¿?


