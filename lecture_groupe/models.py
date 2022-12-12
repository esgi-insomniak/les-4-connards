from django.db import models

from books.models import Books

class LectureGroupes(models.Model):
    lieux = models.CharField(max_length=255)
    date = models.DateField()
    heure = models.TimeField()
    livre = models.ForeignKey(Books, on_delete=models.CASCADE)
    participants = models.IntegerField()
    def __str__(self):
        return self.lieux + " " + str(self.date) + " " + str(self.heure) + " " + str(self.livre) + " " + str(self.participants)