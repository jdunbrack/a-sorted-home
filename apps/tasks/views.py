from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    this_user = User.objects.get(id=request.session['uid'])
    tasks = Task.objects.filter(home__id=this_user.home.id)

    context = {
        "user": this_user,
        "tasks": tasks,
    }

    return render(request,"tasks/index.html", context)

def create(request):
    # only add to db if home exists
    if request.method == "GET":
        return redirect('/tasks/')
    
    this_user = User.objects.get(id=request.session['uid'])
    this_home = this_user.home

    new_task = Task.objects.create(name=request.POST['name'], description=request.POST['desc'], home=this_home)

    return render(request, "tasks/task-partial.html", { 'task': new_task })

def assign(request):
    if request.method == "GET":
        return redirect('/tasks/')

    this_task = Task.objects.get(id=request.POST['task-id'])
    this_task.worker = User.objects.get(id=request.POST['receiver'])
    this_task.save()
    
    return HttpResponse("query success")

def finish(request):
    pass
