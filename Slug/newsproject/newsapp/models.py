from django.db import models
from django.utils.text import slugify


class News(models.Model):
    news_title = models.CharField(max_length = 50,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True)
    news_slug=models.SlugField(max_length=50,blank=True)
    
    def __str__(self):
        return self.news_title 
    
    def save(self, *args, **kwargs):
        self.news_slug = slugify(self.news_title)
        super(News, self).save(*args, **kwargs)