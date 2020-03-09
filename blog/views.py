import json
from email import message

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from blog.models import Comment, Post, User

# Create your views here.

def mylogin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect username or password.')
            return redirect('login')
    else:
        return render(request, template_name='login.html')
    

def mylogout(request):
    logout(request)
    return redirect('login')

def signup(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password==password:
            user = User.objects.create(username=username, password=password, email=email, first_name=fname, last_name=lname)
            user.save();
            return redirect('login')
            
        else:
            return redirect('login')
    return render(request, template_name='signup.html')

def mymain(request):
    return render(request, template_name='index.html')
