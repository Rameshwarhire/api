from django.db import models
from django.utils import timezone
#to set author id from user table we need to add below import
from django.contrib.auth.models import User

from django.urls import reverse
#use after custome user model
from simpleblog import settings
User=settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    #need author having relation with users table in Django database
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
"""
    #this class is use for change admin panal table name
    class Meta:
        verbose_name_plural="student"
"""