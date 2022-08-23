from django.shortcuts import render

def setsession(request):
    request.session['name']='Rahul'
    request.session['lname']='yadav'
    request.session.set_expiry(60)
    return render(request,'stemplate/setsession.html')


def getsession(request):
    #name=request.session['name']
    name=request.session.get('name',default='deleted successfully')
    keys=request.session.keys()
    items=request.session.items()
    #age=request.session.setdefault('age','20')
    
    
    
    
    return render(request,'stemplate/getsession.html',{'name':name,'keys':keys,'items':items})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        request.session.flush()
        
    return render(request,'stemplate/delsession.html')