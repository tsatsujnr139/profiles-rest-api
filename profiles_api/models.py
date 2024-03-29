from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)
from django.conf import settings

# Create your models here.


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, name, password=None):
        """creates a new user profile

        Arguments:
            email {[type]} -- [description]
            name {[type]} -- [description]

        Keyword Arguments:
            password {[type]} -- [description] (default: {None})
        """
        if not email:
            raise ValueError('Email is a required field')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)
        
        return user

    def create_superuser(self, email, name, password):
        """creates a new user profile

        Arguments:
            email string -- [description]
            name string -- [description]

        Keyword Arguments:
            password alphanumeric -- [description] (default: {None})
        """
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using=self.db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database model for user

    Arguments:
        AbstractBaseUser {[type]} -- [description]
        PermissionsMisxin {[type]} -- [description]
    """
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user
        """
        return self.name

    def get_short_name(self):
        """retrieve short name of user
        """
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    """ Profile status update """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    status_text = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.status_text