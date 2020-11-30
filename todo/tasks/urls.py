from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.index,name='todo'),
    path('', views.home, name='home'),
    path('students_form/', views.students_form, name='students_form'),
    path('student_info/<int:studentid>/', views.student_info, name='student_info'),
    path('update/<int:studentid>/', views.update, name='update'),
    path('delet/<int:studentid>/', views.delet, name='delet'),



    
]
