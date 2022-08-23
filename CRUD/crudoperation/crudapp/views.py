from django.shortcuts import render,redirect
from django.http import HttpResponse
from crudapp.models import Student
from crudapp.forms import StudentForm

# Create your views here.
def index(request):
    if request.method =='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ci=fm.cleaned_data['city']
            co=fm.cleaned_data['contact']
            deepak=Student(name=nm,email=em,city=ci,contact=co)
            deepak.save()
            return redirect('show')
     
    else:
        fm=StudentForm()

    return render(request,'home.html',{'form':fm})
 
def show(request,):
    pi=Student.objects.all()
    return render(request,'show.html',{'data':pi})  

def delete(request,id):
    pi=Student.objects.get(pk=id)
    pi.delete()
    return redirect('show')

def update(request,id):
    if request.method == 'POST':
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST ,instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('show')
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi) 
    return render(request,'update.html',{'form':fm})  



