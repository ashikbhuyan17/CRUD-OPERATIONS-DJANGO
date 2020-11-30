from django.shortcuts import render, redirect

from .models import Task,Student
from .forms import TaskForm,studentsForm


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('todo')
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'list.html', context)


def students_form(request):
    sform=studentsForm() 
    if request.method == "POST" :
        sform=studentsForm(request.POST)
        if sform.is_valid():
            sform.save()
            return redirect(home)
    context={
        'title':"studentForm",
        "sform": sform,
    }
    return render(request,'students_form.html',context)  

def home(request):
    student_list= Student.objects.order_by('firstName')
    context={
        'title':"home",
        'student_list':student_list

    }
    return render(request,'home.html',context)


def student_info(request,studentid):
    student_info = Student.objects.get(pk=studentid)
    context={
        'student_info':student_info,
    }
    
    return render(request, 'student_info.html',context)
    

def update(request,studentid):
    student_info = Student.objects.get(pk=studentid)
    
    updateForm=studentsForm(instance=student_info) 
    if request.method == "POST" :
        updateForm=studentsForm(request.POST,instance=student_info)
        if updateForm.is_valid():
            updateForm.save()
            return redirect(home)
    context={
        'title':"updateForm",
        "updateForm": updateForm,
    }
    return render(request, 'update.html', context)
    

def delet(request,studentid):
    student_info = Student.objects.get(pk=studentid).delete()
    context={
        'title':"DeletInfo",
        "delet_message": "Delet Done",
    }
    return render(request, 'delet.html', context)
    

