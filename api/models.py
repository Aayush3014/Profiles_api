from django.db import models

# Below imports are made to override the User model of Django.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    
    """It will manage the User Profiles for the new custom model we have made."""
    
    def create_user(self, email, name, password=None):
        """It will create new users by using the new custom user model."""
        if not email:
            raise ValueError("User must have an email address.")
        
        
        # This will make second half of email lower case for all the emails for user's convinience.
        email = self.normalize_email(email)
        
        # This model will use the model in which the UserProfileManager class is being used.
        user = self.model(email=email, name=name)
        
        
        # This set_password function is used to encrypt the password amd save it instead of saving it in string form.
        user.set_password(password)
        
        # This will save the user in the database that is defined in the settings.py file (using=self._db)
        user.save(using=self._db)
        
        return user
    
    
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with the given details. """
        
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database Model for users"""
    email =  models.EmailField(max_length=200, unique = True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    
    # This line of code is used to manage custom user model from CLI.
    objects = UserProfileManager()
    
    
    # This will ask for email instead of username in django admin login page.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    
    def get_full_name(self):
        """Retrieve Full name of user."""
        return self.name
    
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    
    def __str__(self):
        """Return String Representation of user in admin panel."""
        return self.email