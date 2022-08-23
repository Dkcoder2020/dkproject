from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api2.models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView


'''

@api_view(['GET'])
def home(request):
    
    student_obj=Student.objects.all()
    serializer=StudentSerializer(student_obj,many=True)
    
    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
    
   serializer=StudentSerializer(data=request.data)
   
   if not serializer.is_valid():
       return Response({'status':403,'message':'Something went wrong','data':serializer.errors})
   serializer.save()
    
   return Response({'status':200,'payload':serializer.data,'message':'you sent'})

@api_view(['PATCH'])
def update_student(request,pk):
    try:
            
        student_obj=Student.objects.get(id=pk)
        print(student_obj)
        serializer=StudentSerializer(student_obj,data=request.data,partial=True)
        
        if not serializer.is_valid():
            return Response({'status':403,'message':'Something went wrong','data':serializer.errors})
        
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'you sent'})
    
    except Exception as e:
        print(e)
        
        return Response({'status':403,'message':'invalid id'})
        


@api_view(['DELETE'])
def delete(request, id):
    task = Student.objects.get(id=id)
    task.delete()

    return Response('Item succsesfully delete!')
    
    '''
    
class StudentAPI(APIView):
        def get(self,request):
            student_obj=Student.objects.all()
            serializer=StudentSerializer(student_obj,many=True)
    
            return Response({'status':200,'payload':serializer.data})
    
    
        def post(self,request):
            
            serializer=StudentSerializer(data=request.data)
   
            if not serializer.is_valid():
                return Response({'status':403,'message':'Something went wrong','data':serializer.errors})
            serializer.save()
    
            return Response({'status':200,'payload':serializer.data,'message':'you sent'})
        
        def put(self,request):
            try:
            
                student_obj=Student.objects.get(id=request.data['id'])
                print(student_obj)
                serializer=StudentSerializer(student_obj,data=request.data)
        
                if not serializer.is_valid():
                    return Response({'status':403,'message':'Something went wrong','data':serializer.errors})
                
                serializer.save()
                return Response({'status':200,'payload':serializer.data,'message':'you sent'})
    
            except Exception as e:
                   print(e)
                
                   return Response({'status':403,'message':'invalid id'})
         
        def patch(self,request):
            
            try:
            
                student_obj=Student.objects.get(id=request.data['id'])
                print(student_obj)
                serializer=StudentSerializer(student_obj,data=request.data,partial=True)
        
                if not serializer.is_valid():
                    return Response({'status':403,'message':'Something went wrong','data':serializer.errors})
                
                serializer.save()
                return Response({'status':200,'payload':serializer.data,'message':'you sent'})
    
            except Exception as e:
                   print(e)
                   return Response({'status':403,'message':'invalid id'})
            
            
            
             
        def delete(self,request):
            task = Student.objects.get(id=request.data['id'])
            task.delete()

            return Response('Item succsesfully delete!')

    
    
            
        
   
