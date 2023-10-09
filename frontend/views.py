from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(TemplateView):
    template_name = "register.html"

class HomeView(TemplateView):
    template_name = "index.html"

class UploadImageView(TemplateView):
    template_name = "upload_image.html"