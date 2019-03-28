from django.shortcuts import render
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
    pass # only add to db if home exists

def assign(request):
    pass # only add to db if home exists

def finish(request):
    pass