from django.db import models

# Create your models here.

class Timetable(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
