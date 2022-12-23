from datetime import timezone
import datetime
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    jaquette = models.URLField(max_length=1000, null=True, blank=True)
    editeur = models.CharField(max_length=255, null=True, blank=True)
    collection = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    Librairie = models.CharField(max_length=255, null=True, blank=True)
    date_emprut = models.DateField(null=True, blank=True)
    date_retour = models.DateField(null=True, blank=True)
    statut = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title