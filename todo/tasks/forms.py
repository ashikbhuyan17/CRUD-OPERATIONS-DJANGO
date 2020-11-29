from django import forms
from .models import Task,Student
from django.forms import ModelForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class studentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
