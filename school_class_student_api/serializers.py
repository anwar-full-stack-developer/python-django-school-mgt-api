from django.db import models
from school_class_api.models import SchoolClass
from rest_framework import serializers  
from .models import SchoolClassStudent
  
class SchoolClassStudentSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=200, required=True)  
    last_name = serializers.CharField(max_length=200, required=True)  
    address = serializers.CharField(max_length=200, required=True)  
    roll_number = serializers.IntegerField()  
    mobile = serializers.CharField(max_length=10, required=True)  
    class_id = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
  
    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return SchoolClassStudent.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.first_name = validated_data.get('first_name', instance.first_name)  
        instance.last_name = validated_data.get('last_name', instance.last_name)  
        instance.address = validated_data.get('address', instance.address)  
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)  
        instance.mobile = validated_data.get('mobile', instance.mobile)  
        instance.class_id = validated_data.get('class_id', instance.class_id)  
  
        instance.save()  
        return instance 
    
    class Meta:  
        model = SchoolClassStudent  
        fields = ('__all__') 