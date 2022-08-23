from multiprocessing import get_all_start_methods
from django.shortcuts import render,redirect
from django.contrib import messages
from playsound import playsound

import random

def index(request):
    if request.method == 'POST':
   
         user=request.POST.get('user')
        
         list=['snake','water','gun']
         com=random.choice(list)
         if(user=='snake' and com=='water'):
            # print("you are win")
            messages.info(request,'you are win')
           # playsound(r'static/images/win.mp3')
        
         elif(user=='water' and com=='snake'):
            #print("you are lose")
            messages.info(request,'you are lose')
           # playsound(r'static/images/loose.mp3')   
        
         elif(user=='snake' and com=='gun'):
            # print("you are lose")
            messages.info(request,'you are lose')
            #playsound(r'static/images/loose.mp3')
        
         elif(user=='water' and com=='gun'):
            # print("you are win")
            messages.info(request,'you are win')
            #playsound(r'static/images/win.mp3')

         elif(user=='gun' and com=='snake'):
            #print("you are win")
            messages.info(request,'you are win')
            playsound(r'static/images/win.mp3')
        
         elif(user=='gun' and com=='water'):
            #print("you are lose")
            messages.info(request,'you are lose')
           # playsound(r'static/images/loose.mp3')
        
         elif(user=='gun' and com=='gun'):
            # print("match draw")
            messages.info(request,"match draw")
            playsound(r'static/images/click.mp3')
        
         elif(user=='snake' and com=='snake'):
            # print("match draw")
            messages.info(request,"match draw") 
            #playsound(r'static/images/click.mp3') 
         elif(user=='water' and com=='water'):
            # print("match draw")
            messages.info(request,"match draw")
           # playsound(r'static/images/click.mp3')
         else:
           # print("enter valid option") 
            messages.info(request,'')
           # playsound(r'static/images/click.mp3')

    return render(request,'index.html')


def color(request):
   if request.method =='POST':
      colors = request.POST['color']
      print(colors)
  
   return render(request,"color.html")
   