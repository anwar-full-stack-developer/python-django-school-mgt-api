from .views import SchoolClassStudentView  
from django.urls import path  
  
urlpatterns =    [  
    path('api/', SchoolClassStudentView.as_view()),  
    path('api/<int:id>/', SchoolClassStudentView.as_view())  
]  