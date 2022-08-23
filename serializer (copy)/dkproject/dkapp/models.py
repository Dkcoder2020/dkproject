from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
        
   
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    city=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)

    def __str__(self):
        return self.name
