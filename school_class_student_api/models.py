from django.db import models
from school_class_api.models import SchoolClass


class SchoolClassStudent(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=10)  
    class_id = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    
    def __str__(self):  
        return self.first_name + " " + self.last_name  
    
