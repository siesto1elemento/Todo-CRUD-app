from django.db import models
from datetime import datetime
from django.urls import reverse    

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length= 30)
    date_added = models.DateTimeField(default= datetime.now)
    completed = models.BooleanField(default= False)
    
    
    def get_absolute_url(self):
        return reverse ('home')
        