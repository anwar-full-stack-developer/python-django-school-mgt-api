from django.db import models

class SchoolClass(models.Model):  
    name = models.CharField(max_length=200)  
    code_number = models.CharField(max_length=200)  
    label = models.CharField(max_length=100)  
  
    def __str__(self):  
        return self.name + "(" + self.code_number  + ")"
    
