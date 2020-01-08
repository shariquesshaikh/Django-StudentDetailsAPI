from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    dob=models.DateField()
    age=models.IntegerField()
    standard=models.CharField(max_length=30)
