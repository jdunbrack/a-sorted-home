from django.shortcuts import render, redirect, HttpResponse
import re
from .models import *
import bcrypt

# Create your views here.
def landing(request):
    return render(request, 'login_reg/index.html')
    
def email_verify(request):
    if request.method == "GET":
        return redirect('/login/')

    data = User.objects.filter(email=request.POST['email'])

    if len(data) > 0:
        return render(request, 'login_reg/email-partial.html', {"valid": False})
    else:
        return render(request, 'login_reg/email-partial.html', {"valid": True})

def pw_verify(request):
    if request.method == "GET":
        return redirect('/login/')

    PW_REGEX = re.compile(r'(?=.*[0-9]+)(?=.*[A-Z]+)(?=.*[a-z]+)')

    pw = request.POST['pw-entry']

    valid = True
    if PW_REGEX.match(pw) == None:
        valid = False
    if pw != request.POST['pw-confirm']:
        valid = False

    return render(request, 'login_reg/pw-partial.html', {"valid": valid})


def add_user(request):
    if request.method == "GET":
        return redirect('/login/')

    if request.POST['login_reg'] == "register":

        NAME_REGEX = re.compile(r'[^\W][\d]')

        if NAME_REGEX.search(request.POST['first-name']) != None or NAME_REGEX.search(request.POST['last-name']) != None:
            return HttpResponse("Invalid")

        PW_REGEX = re.compile(r'(?=.*[0-9]+)(?=.*[A-Z]+)(?=.*[a-z]+)')
        pw = request.POST['pw-entry']

        if PW_REGEX.match(pw) == None:
            return redirect('/login/')
        
        user_pw = bcrypt.hashpw(request.POST['pw-entry'].encode(), bcrypt.gensalt())

        new_user = User.objects.create(first_name=request.POST['first-name'], last_name=request.POST['last-name'],\
            email=request.POST['email'], password=user_pw.decode())

        if len(request.POST['join-id']) > 0:
            # handle joining existing home
            new_user.home.add(Home.objects.get(join_id=request.POST['join-id']))

        request.session['uid'] = new_user.id

        return redirect('/users/dash')

    else:
        user = User.objects.filter(email=request.POST['email'])

        if len(user) != 1:
            return HttpResponse("Invalid")
        else:
            user = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['uid'] = user.id
            return HttpResponse("Valid")
        else:
            return HttpResponse("Invalid")

def logout(request):
    request.session.clear()
    return redirect('/')

def age_verify(request):
    thirteen_years = datetime.timedelta(days=4748)
    birthday = datetime.datetime.strptime(request.POST['birthday'], "%Y-%m-%d")
    birthday = birthday.date()

    valid = True
    if (datetime.date.today() - birthday) < thirteen_years:
        valid = False

    return render(request,'login_reg/age-partial.html', {"valid": valid})

def name_verify(request):
    if request.POST['login_reg'] == 'register':
            
        NAME_REGEX = re.compile(r'[^\W][\d]')

        if NAME_REGEX.search(request.POST['first-name']) != None or NAME_REGEX.search(request.POST['last-name']) != None:
            valid = False
        else:
            valid = True

        return render(request, 'login_reg/name-partial.html', {"valid": valid})

    else:
        return redirect('/')