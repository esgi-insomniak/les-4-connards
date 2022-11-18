from datetime import timezone
import datetime
from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    published_date = models.DateField('date published')
    
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)
    
