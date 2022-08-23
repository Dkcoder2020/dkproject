from django.db import models

class Game(models.Model):
    CATEGORY =(
        ('snake','snake'),
        ('water','water'),
        ('gun','gun'),
        )
   
    user = models.CharField(max_length=50,choices=CATEGORY)
    def __str__(self):
        return self.user
    