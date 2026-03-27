from django.shortcuts import render, redirect
from .models import Task


def index(request):
    if request.method == 'POST':
        text = request.POST.get('task')
        if text:
            Task.objects.create(text=text)
        return redirect('index')

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/index.html', {'tasks': tasks})


def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = True
    task.save()
    return redirect('index')


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')