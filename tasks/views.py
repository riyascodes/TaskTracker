# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.db.models import Q

def dashboard(request):
    search_query = request.GET.get('search', '')
    tasks = Task.objects.all()

    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    sort_by = request.GET.get('sort', 'due_date')
    if sort_by == 'priority':
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
        tasks = sorted(tasks, key=lambda t: priority_order[t.priority_level])
    else:
        tasks = tasks.order_by('due_date')

    context = {'tasks': tasks, 'search_query': search_query}
    return render(request, 'tasks/dashboard.html', context)

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST['due_date']
        priority_level = request.POST['priority_level']
        Task.objects.create(title=title, description=description, due_date=due_date, priority_level=priority_level)
    return redirect('dashboard')

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # Save updates
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.due_date = request.POST['due_date']
        task.priority_level = request.POST['priority_level']
        task.save()
        return redirect('dashboard')
    # GET request: show edit form
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('dashboard')

def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('dashboard')
