from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile', default='/media/profile/profile_default.jpg', null=True)