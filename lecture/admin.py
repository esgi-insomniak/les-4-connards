from django.contrib import admin

# Register your models here.

from .models import Lecture

admin.site.register(Lecture)