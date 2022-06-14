from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weigth = models.FloatField()
    sex = models.CharField(max_length=15)