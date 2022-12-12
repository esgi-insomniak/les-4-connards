from django.db import models

from books.models import Books


class Librairie(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    livres = models.ManyToManyField(Books)
    def __str__(self):
        return self.nom