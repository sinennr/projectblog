import json
from builtins import object
from email import message

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import PostForm

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

def sign_up(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')

        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save
            return redirect('index')
        else:
            context['error'] = 'Password Not Match!!!'
            return render(request, template_name='signup.html', context=context)
    
    return render(request, template_name='signup.html', context=context)

def mymain(request):
    search = request.GET.get('search', '')

    post_list = Post.objects.all()
    if search != '':
        post_list = Post.objects.filter(title__icontains=search)
    
    context = {
        'search': search,
        'post_list':post_list,
    }

    return render(request, template_name='index.html',context=context)

def post_detail(request,id):
    post_detail = Post.objects.get(pk=id)
    context = {
        'post_detail': post_detail,
    }
    return render(request, template_name='detail.html',context=context)

def createpost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.title = request.tile
            # post.content = request.content
            post.save()
            return redirect('index', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

# def add_post(request):
    
#     if request.method == 'POST':
#         if request.POST.get('title') != '':
#             post = Post.objects.create(
#                 title = request.POST.get('title'),
#                 content = request.POST.get('content')
#             )
            
#     else:
#         post = Post.objects.none()
#         messages.info(request,'Please Add Post')

#     return render(request, template_name='index.html',context=context)

# def add_comment(request):
#     if request.method == 'POST':
#         if request.POST('comment') != '':
#             add_comment = Comment.objects.create(
#                 content = request.POST('content')

#             )