from django.contrib import admin

from .models import Books
from librairie.models import Librairie
from .models import Loan

admin.site.register(Books)
admin.site.register(Librairie)
admin.site.register(Loan)
