from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weigth = models.FloatField()
    sex = models.CharField(max_length=15)
    group = models.ForeignKey(
        "groups.Group", on_delete=models.CASCADE, related_name="groups"
    )
    characteristics= models.ManyToManyField(
        "characteristics.Characteristic", related_name="characteristics"
    )
