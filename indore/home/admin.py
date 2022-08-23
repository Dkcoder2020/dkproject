from django.contrib import admin
from home.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','eemail','econtact']
admin.site.register(Employee,EmployeeAdmin)


# Register your models here.

    