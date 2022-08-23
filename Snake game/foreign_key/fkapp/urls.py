from django.contrib import admin
from django.urls import path
from fkapp import views

urlpatterns = [
   
    path("",views.index, name='index'),
    path("color/",views.color, name='color')
]
