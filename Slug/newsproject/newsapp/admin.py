from django.contrib import admin
from newsapp.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=['news_title','description','news_slug']
    
admin.site.register(News,NewsAdmin)
