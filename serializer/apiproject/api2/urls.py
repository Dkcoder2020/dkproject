from django import views
from django.contrib import admin
from django.urls import path,include
from api2 import views



urlpatterns = [
   # path('',views.home,name='home'),
   # path('student/',views.post_student,name='student'),
   # path('update/<int:pk>',views.update_student,name='update'),
   # path('del/<int:id>',views.delete,name='del'),
    
    path('student/',views.StudentAPI.as_view(),name='studentapi')
]
