from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .manager import UserManager


# Create your models here.


class CustomeUser(AbstractUser):

	username=None
	phone_number = models.CharField(max_length=15, unique=True)
	email=models.EmailField(unique=True)
	profile_image=models.FileField(upload_to='profile_img')

	USERNAME_FIELD='phone_number'
	REQUIRED_FIELD=[]
	objects=UserManager()
