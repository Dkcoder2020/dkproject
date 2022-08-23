from rest_framework import serializers
from .models import Task,Image

class TaskSerializer(serializers.ModelSerializer):
			class Meta:
				model = Task
				fields ='__all__'
    
    
class ImageSerializer(serializers.ModelSerializer):
            class Meta:
                model = Image
                fields ='__all__'