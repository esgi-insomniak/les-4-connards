from django.db import models
from django.contrib.postgres.fields import ArrayField

from books.models import Books
from librairie.models import Librairie

class LectureGroupes(models.Model):
    lieux = models.CharField(max_length=255)
    date = models.DateField()
    heure = models.TimeField()
    livre = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, blank=True)
    participants = ArrayField(models.CharField(max_length=255, blank=True), null=True, blank=True)
    librairie = models.ManyToOneRel(Librairie, on_delete=models.CASCADE, to=Librairie, related_name='librairie', field_name='librairie')
    def __str__(self):
        return self.lieux + " " + str(self.date) + " " + str(self.heure) + " " + str(self.livre) + " " + str(self.participants)