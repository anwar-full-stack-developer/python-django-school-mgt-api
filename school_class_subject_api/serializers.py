from django.db import models
from school_class_api.models import SchoolClass

from rest_framework import serializers  
from .models import SchoolClassSubject

class SchoolClassSubjectSerializer(serializers.ModelSerializer):  
    name = serializers.CharField(max_length=200, required=True)  
    # class_id = serializers.CharField(required=True)
    class_id = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def create(self, validated_data):  
        """ 
        Create and return a new `Class` instance, given the validated data. 
        """  
        return SchoolClassSubject.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Class` instance, given the validated data. 
        """  
        instance.name = validated_data.get('name', instance.name)  
        instance.class_id = validated_data.get('class_id', instance.class_id)  
  
        instance.save()  
        return instance 
    
    class Meta:  
        model = SchoolClassSubject  
        fields = ('__all__') 
  