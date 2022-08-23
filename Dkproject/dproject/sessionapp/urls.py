from django.contrib import admin
from django.urls import path
from sessionapp import views


urlpatterns = [
        
        path('',views.setsession),
        path('get/',views.getsession),
        path('del/',views.delsession),



]
