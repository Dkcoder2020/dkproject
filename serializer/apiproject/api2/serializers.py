from rest_framework import serializers
from api2.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
       # exclude=['id']
       
    
    def validate(self,data):
    
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'Name does not contains integer values'})
       
        if data['age']< 18:
            raise serializers.ValidationError({'error':'Age should above 18 years'})
        
        return data