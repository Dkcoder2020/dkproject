from django.db import models
from django.forms import ImageField

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    def __str__(self):
        return self.title
