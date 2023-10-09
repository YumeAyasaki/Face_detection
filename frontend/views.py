from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(TemplateView):
    template_name = "register.html"

class HomeView(TemplateView):
    template_name = "index.html"

@login_required
class UploadImageView(TemplateView):
    template_name = "upload_image.html"