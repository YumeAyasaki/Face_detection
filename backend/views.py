from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    # print(username, password)

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login')
    
def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirmPassword']

    # Check if the username is existed
    if User.objects.filter(username=username).exists() or password != confirm_password:
        return HttpResponseRedirect('/register')
    else:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return HttpResponseRedirect('/login')
    

@login_required    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def upload_image(request):
    pass