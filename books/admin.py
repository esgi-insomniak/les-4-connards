from django.contrib import admin

from .models import Books
from librairie.models import Librairie

admin.site.register(Books)
admin.site.register(Librairie)
