from django.shortcuts import render,redirect
from . import forms
from .models import Task

# Create your views here.
def add_task(request):
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    
    task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form': task_form})

def show_task(request):
    data = Task.objects.all()
    return render(request, 'show_task.html', {'data':data})



def edit_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
   
    return render(request, 'add_task.html', {'form': task_form})



def delete_task(request,id):
    post = Task.objects.get(pk=id)
    post.delete()
    return redirect("show_task")