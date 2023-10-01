from django.db import models
from school_class_api.models import SchoolClass

class SchoolClassSubject(models.Model):  
    name = models.CharField(max_length=200)
    class_id = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):  
        return self.name