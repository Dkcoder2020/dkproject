from django.shortcuts import render
from newsapp.models import News
from newsapp.forms import NewsForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        fm=NewsForm(request.POST)
        if fm.is_valid():
            ti=fm.cleaned_data['news_title']
            des=fm.cleaned_data['description']
            ns=fm.cleaned_data['news_slug']
            
            deepak=News(news_title=ti,description=des,news_slug=ns)
            deepak.save()
        
          
    else:
        fm=NewsForm()
    return render(request, 'index.html',{'form':fm})

def show(request):
    pi=News.objects.all()
    return render(request, 'table.html',{'data':pi})

def newsslug(request,dkslug):
    pi=News.objects.get(news_slug=dkslug)
    fm=NewsForm(instance=pi) 
    return render(request,'slugtable.html',{'form':fm})