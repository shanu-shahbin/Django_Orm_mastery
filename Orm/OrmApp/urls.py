from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    path('', views.Home, name='home'), 
    path('students/', views.students, name='students'),
    path('students_details/', views.students_details, name='students_details')
]
