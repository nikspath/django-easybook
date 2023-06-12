from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=100)
	age =  models.IntegerField(null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	pass


class Car(models.Model):
	car_name=models.CharField(max_length=100)
	car_speed=models.IntegerField()

	def __str__(self):
		return self.car_name


@receiver(post_save,sender=Car)
def call_car_api(sender,instance, **kwargs):
	print("call create api ")
	print(sender,instance,kwargs)


@receiver(pre_save,sender=Car)
def call_car_api_pre(sender,instance,**kwargs):
	print("pre api call")

