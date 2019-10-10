from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """database model for user
    
    Arguments:
        AbstractBaseUser {[type]} -- [description]
        PermissionsMisxin {[type]} -- [description]
    """
    email = models.EmailField(max_length=254,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']