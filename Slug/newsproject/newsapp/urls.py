from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('show/',views.show,name='show'),
    path('newsslug/<slug:dkslug>/',views.newsslug,name='newsslug'),

]
