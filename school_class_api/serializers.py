from rest_framework import serializers  
from .models import SchoolClass

class SchoolClassSerializer(serializers.ModelSerializer):  
    name = serializers.CharField(max_length=200, required=True)  
    code_number = serializers.CharField(max_length=200, required=True)
    label = serializers.CharField(max_length=100, required=True)  


    def create(self, validated_data):  
        """ 
        Create and return a new `Class` instance, given the validated data. 
        """  
        return SchoolClass.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Class` instance, given the validated data. 
        """  
        instance.name = validated_data.get('name', instance.name)  
        instance.code_number = validated_data.get('code_number', instance.code_number)  
        instance.label = validated_data.get('label', instance.label)  
  
        instance.save()  
        return instance 
    class Meta:  
        model = SchoolClass  
        fields = ('__all__') 
  