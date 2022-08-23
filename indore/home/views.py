
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render ,redirect
from home.models import Employee    
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def welcome(request):
    return render(request,'home.html')

def form1(request):
    if request.method == 'POST':
        id = request.POST['eid']
        name = request.POST['ename']
        email =request.POST['eemail']
        contact =request.POST['econtact']
        # if int(id) < 500:
        #     return HttpResponse('error id')
        # else:
        deepak=Employee(eid=id,ename=name,eemail=email,econtact=contact)
        deepak.save()
             
    return render(request,'index.html')

def show(request):  
    obj = Employee.objects.all()
    return render(request, "show.html",{'obj':obj})
    

def delete(request,id): 
    obj = Employee.objects.get(id=id)
    obj.delete()
    return redirect('show')

  
def update(request,pk):
    obj1 = Employee.objects.get(id=pk)
    if request.method == 'POST':
        id = request.POST['eid']
        name = request.POST['ename']
        email =request.POST['eemail']
        contact =request.POST['econtact']
        
        obj = Employee.objects.get(id=pk)
        obj.eid = id
        obj.ename = name
        obj.eemail = email
        obj.econtact = contact
        obj.save()
        return redirect('show')
    return render(request,'update.html',{'obj1' : obj1})

def search(request):
    given_name= request.POST['pk']
    obj=Employee.objects.filter(ename=given_name)
    return render(request,'show.html',{'obj':obj})
    