from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

class ProfileImage(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    
    def __unicode__(self):
        return self.user.username
    
