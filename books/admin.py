from django.contrib import admin

from .models import Books
from lecture_groupe.models import LectureGroupes
from librairie.models import Librairie

admin.site.register(Books)
admin.site.register(LectureGroupes)
admin.site.register(Librairie)
