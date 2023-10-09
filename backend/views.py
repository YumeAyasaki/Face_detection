from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

import cv2

# Create your views here.
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

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

    User = get_user_model()

    # Check if the username is existed
    if User.objects.filter(username=username).exists() or password != confirm_password:
        return HttpResponseRedirect('/register')
    else:
        user = User.objects.create_user(username=username, password=password, profile_image=None)
        user.save()
        return HttpResponseRedirect('/login')
    

@login_required    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def upload_image(request):
    image = request.FILES['profile_image']

    user = request.user
    user.profile_image = image
    user.save()

    return HttpResponseRedirect('/')

@login_required
def face_detection(request):
    user = request.user
    original_image = user.profile_image

    def face_bounding_box(image):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
        
        return image
    
    face_image = face_bounding_box(original_image)
    
    # Return as a response
    response = HttpResponse(content_type='image/jpeg')
    cv2.imwrite(response, face_image)
    return response