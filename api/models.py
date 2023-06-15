from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll = models.IntegerField(primary_key=True)
    City = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name