from django.db import models
from django.contrib.postgres.fields import ArrayField

class Librairie(models.Model):
    nom = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.nom