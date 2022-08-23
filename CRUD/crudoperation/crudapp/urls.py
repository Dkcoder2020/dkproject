from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [

path("",views.index,name='home'),
path("show/",views.show,name='show'),
path("delete/<int:id>/",views.delete,name='del'),
path("update/<int:id>/",views.update,name='update'),


]
