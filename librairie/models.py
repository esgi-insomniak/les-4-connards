from django.db import models
from django.contrib.postgres.fields import ArrayField

from books.models import Books


class Librairie(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    #livres = models.ArrayField(models.CharField(max_length=255, blank=True))
    def __str__(self):
        return self.nom