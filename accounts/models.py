from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
#add in settings.py
# Create your models here.
class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,password,**extra_fields):
        email = self.normalize_email(email)
        user= self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff field value as a true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser field value a true")
         
        return self.create_user(email=email,password=password,**extra_fields)
    
class User(AbstractUser):
    email=models.CharField(max_length=100,unique=True)
    username=models.CharField(max_length=50)
    dob=models.DateField(null=True)

    objects=CustomUserManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.username    


      