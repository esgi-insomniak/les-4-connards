from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from books.models import Books
from librairie.models import Librairie

class Lecture(models.Model):
    lieux = models.CharField(max_length=255)
    date = models.DateField()
    heure = models.TimeField()
    Books = models.ForeignKey(Books, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='lectures', blank=False, default=[], null=True)
    Librairie = models.ForeignKey(Librairie, on_delete=models.CASCADE)

    def __str__(self):
        return self.lieux + " " + str(self.date) + " " + str(self.heure) + " " + str(self.Books) + " " + str(self.participants)