from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

import os
import cv2
import numpy as np
from django.http import JsonResponse
import base64
import io

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
    media_root = settings.MEDIA_ROOT

    user = request.user
    original_image = os.path.join(media_root, user.profile_image.name)

    def face_bounding_box(image):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Try to convert the image to a NumPy array.
        image = cv2.imread(image)
        try:
            image = np.asarray(image)
        except Exception as e:
            # If the conversion fails, log the error and return the original image.
            print(e)
            return image
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print(faces)

        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
        
        return image
    
    face_image = face_bounding_box(original_image)
    face_image_name = user.profile_image.name.split('.')[0] + '_face.' + user.profile_image.name.split('.')[1]
    face_image_path = os.path.join(media_root, face_image_name)
    print(face_image_path)
    cv2.imwrite(face_image_path, face_image)

    user.profile_image = face_image_name
    user.save()

    return HttpResponseRedirect('/')