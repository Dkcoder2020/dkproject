from django.db import models

class Employee(models.Model):
    eid=models.IntegerField(null=True, default="")
    ename=models.CharField(max_length=100)
    eemail=models.CharField(max_length=50)
    econtact=models.CharField(max_length=20)

    
  
  