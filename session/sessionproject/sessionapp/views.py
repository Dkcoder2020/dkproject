from django.shortcuts import render,redirect
from sessionapp.models import Student

from django.contrib import messages

def reg(request):
    if request.method == 'POST':
        nm=request.POST['name']
        em=request.POST['email']
        ci=request.POST['city']
        con=request.POST['contact']
        pas=request.POST['password']
        form=Student(name=nm,email=em,city=ci,contact=con,password=pas)
        form.save()
        return redirect('loginpage') 
    return render(request,'registation.html')

def login(request):
    
    if request.method =='POST':
        try:
            deepak=Student.objects.get(name=request.POST['name'],password=request.POST['password'])
            
            if request.session:
                request.session['name']=deepak.name
                return redirect('homepage')
            else:
                return redirect('login')
        except Student.DoesNotExist as e:
            messages.success(request,"Username /Password invalid..")
               
    return render(request,'index.html')


def logout(request):
    try:
      del request.session['name']
    except:
        redirect('loginpage')
    return redirect('loginpage')

def home(request):

    return render(request,'home.html')

