from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        else:
            form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})


def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('todo_list')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('todo_list')
