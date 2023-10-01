from .views import SchoolClassView 
from django.urls import path  
  
urlpatterns =    [  
    path('api/', SchoolClassView.as_view()),  
    path('api/<int:id>/', SchoolClassView.as_view())  
]  