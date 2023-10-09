from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(TemplateView):
    template_name = "register.html"

class HomeView(TemplateView):
    template_name = "index.html"

@method_decorator(login_required, name='dispatch')
class FaceDetectionView(TemplateView):
    template_name = "face_detection.html"