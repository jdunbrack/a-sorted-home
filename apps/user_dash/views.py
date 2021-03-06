from django.shortcuts import render, redirect, HttpResponse
from .models import *
from apps.login_reg.models import User, JoinedDate
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import os
import bcrypt
import re
import random
import string


def index(request):
    if not 'uid' in request.session:
        return redirect('/login/')
    
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')
    this_user = this_user[0]

    if not this_user.home:
        context = {
            'user': this_user,
        }
    else:
        context = {
            'user': this_user,
            'this_home': this_user.home,
        }

    return render(request, 'user_dash/index.html', context)

def edit_user(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')

    context = {
        'user': this_user[0],
    }

    return render(request, 'user_dash/update.html', context)

def upload_image(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')

    this_user = this_user[0]

    IMAGE_REGEX = re.compile(r'^image')

    if IMAGE_REGEX.match(request.files['profile-pic'].content_type) == None:
        messages.error("Please upload an image file.")
        return redirect('/users/dash')

    save_name = str(request.session['uid']) + "_" + create_join_id() + create_join_id() + request.FILES['profile-pic'].name[-4:]

    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', save_name) 
    path = default_storage.save(save_path, request.FILES['profile-pic'])
    this_user.profile_pic = "/media/uploads/" + save_name 
    this_user.save()
    return redirect('/users/dash')

def update_user(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')

    this_user = this_user[0]
    this_user.first_name = request.POST['first-name']
    this_user.last_name = request.POST['last-name']
    this_user.email = request.POST['email']

    this_user.save()

    return redirect('/users/dash')


def pw_verify(request):
    if request.method == "GET":
        return redirect('/users/dash/edit')

    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')

    this_user = this_user[0]

    if 'password' in request.POST:
        password = request.POST['password']
    elif 'current-pw' in request.POST:
        password = request.POST['current-pw']

    valid = False
    if bcrypt.checkpw(password.encode(), this_user.password.encode()):
        valid = True

    return render(request, 'user_dash/pw-partial.html',{'valid': valid})

def pw_validate(request):
    if request.method == "GET":
        return redirect('/login')

    PW_REGEX = re.compile(r'(?=.*[0-9]+)(?=.*[A-Z]+)(?=.*[a-z]+)')

    pw = request.POST['new-pw']

    valid = True
    if PW_REGEX.match(pw) == None:
        valid = False
    if pw != request.POST['new-pw-confirm']:
        valid = False

    return render(request, 'user_dash/new-pw-partial.html', {"valid": valid})

def pw_update(request):
    if request.method == "GET":
        return redirect('/users/dash')
    
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')

    this_user = this_user[0]

    PW_REGEX = re.compile(r'(?=.*[0-9]+)(?=.*[A-Z]+)(?=.*[a-z]+)')

    pw = request.POST['new-pw']

    if PW_REGEX.match(pw) == None:
        return redirect('/users/dash/edit')
    if pw != request.POST['new-pw-confirm']:
        return redirect('/users/dash/edit')

    user_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

    this_user.password = user_pw.decode()
    this_user.save()

    return redirect ('/users/dash')

def edit_payment(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')

    this_user = this_user[0]

    url = request.POST['payment-url']
    test = re.compile(r'/$')
    if test.match(url):
        url = url[:-1]

    this_user.payment_url = url
    this_user.save()

    return redirect('/users/dash')

def create_home(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')

    this_user = this_user[0]

    new_home = Home.objects.create(name=request.POST['name'])

    while len(Home.objects.filter(join_id=new_home.join_id)) > 1:
        new_home.join_id = create_join_id()

    new_home.owner.add(this_user)
    new_home.members.add(this_user)
    new_home.save()
    new_jd = JoinedDate.objects.create(member=this_user, home=new_home)
    new_jd.save()

    return redirect('/users/dash')

def join_home(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')
    this_user = this_user[0]

    Home.objects.get(join_id=request.POST['join-id']).members.add(this_user)
    return redirect('/users/dash')

def delete_home(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')
    this_user = this_user[0]

    if this_user.id != this_user.home.owner.first().id:
        return redirect('/users/dash')

    this_home = Home.objects.get(owner__id=this_user.id)
    this_home.delete()
    this_user.my_home = None
    return redirect('/users/dash')

def leave_home(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')
    this_user = this_user[0]

    this_user.home = None
    return redirect('/users/dash')

def edit_home(request):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')
    this_user = this_user[0]
    this_home = this_user.my_home

    if request.method == "GET":
        return render(request, "user_dash/edit-home.html", {'this_home': this_home})

    this_home.name = request.POST['name']
    return redirect('/users/dash')

def remove_member(request, user_id):
    this_user = User.objects.filter(id=request.session['uid'])

    if len(this_user) != 1:
        request.session.clear()
        return redirect('/')
    this_user = this_user[0]

    remove_user = User.objects.get(id=user_id)
    remove_user.home = None
    remove_user.save()

    return redirect('/users/dash')

def base_redir(request):
    return redirect('/users/dash') 
