from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.


def dashboard(request):
    tasks = Task.objects.all().order_by('-created_date')
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/dashboard.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/dashboard.html', {'form': form, 'task': task, 'tasks': Task.objects.all()})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('dashboard')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('dashboard')
