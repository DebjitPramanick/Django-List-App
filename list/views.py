from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def index(req):
    tasks = Task.objects.all

    if req.method == 'POST':
        newTask = Task(title = req.POST['title'])
        newTask.save()
        print(req.POST['title'])
        return redirect('/')

    return render(req, 'index.html', {'tasks': tasks})

def check(req, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')