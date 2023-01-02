from datetime import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User

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
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

class Loan(models.Model):
    date_retour = models.DateField(null=True, blank=True)
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.borrowed_by.username + " " + self.book.title