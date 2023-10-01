from .views import SchoolClassSubjectView
from django.urls import path  
  
urlpatterns =    [  
    path('api/', SchoolClassSubjectView.as_view()),  
    path('api/<int:id>/', SchoolClassSubjectView.as_view())  
]  