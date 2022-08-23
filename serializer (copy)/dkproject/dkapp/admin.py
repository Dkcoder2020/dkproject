from django.contrib import admin
from dkapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']
admin.site.register(Student,StudentAdmin)

