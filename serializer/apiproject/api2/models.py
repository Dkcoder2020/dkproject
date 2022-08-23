from django.db import models

class Student(models.Model):
    name= models.CharField(max_length = 150)
    age= models.IntegerField(default=10)
    father= models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name    
