from django.contrib import admin
from django.urls import path
from dkapp import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer/<int:pk>/',views.customer,name='customer'),
    path('createorder/<int:pk>/',views.createorder,name='createorder'),
    path('update_order/<int:pk>/',views.updateorder,name='update_order'),
    path('delete_order/<int:pk>/',views.deleteorder,name='delete_order'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('user/',views.user,name='user'),
    
]

