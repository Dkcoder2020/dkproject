from django.shortcuts import render
from django.http import HttpResponse
from dkapp.models import Student
from .forms import StudentForm
from dkapp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer


def tasklist(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return render(request,'index.html',{'data': serializer.data})

def taskdetail(request,id):
    stu=Student.objects.get(id=id)

    serializer=StudentSerializer(stu,many=False)
    return render(request,'index.html',{'data': serializer.data })