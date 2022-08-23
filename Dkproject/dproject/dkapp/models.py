from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    CATEGORY =(
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
        )
    name=models.CharField(max_length=50)
    price=models.FloatField()
    category=models.CharField(max_length=50,choices=CATEGORY)
    description=models.CharField(max_length=50)
    date_created=models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name
  
    
class Order(models.Model):  
    STATUS =(
        ('Pending','Pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivereds','Delivereds'),
        )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product =models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 200,choices=STATUS)
    
    
    
    