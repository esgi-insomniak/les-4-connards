from django import forms
from .models import Lecture

class LectureForm(forms.Form):
    class Meta:
        model = Lecture
        fields = ['librairie', 'date', 'heure', 'books', 'lieux']