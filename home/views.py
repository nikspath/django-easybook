from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import random


# Create your views here.

peoples=[
	{'name':'nikhil','age':34},
	{'name':'raj','age':4},
	{'name':'ganesh','age':14},
	{'name':'ramesh','age':54},
	{'name':'om','age':45},
]



def send_email_to_client():
	message="this is test from fjsnog"
	subject="test django"
	from_host = settings.EMAIL_HOST_USER
	to=['patilnikhil991@gmail.com']
	send_mail(subject,message,from_host,to)	
	return redirect("/")

def home(request):
	#send_email_to_client()
	Car.objects.create(car_name="eon",car_speed=random.randint(50,150))
	return HttpResponse("Hi nikhil home")

def homewithhH1(request):
	return HttpResponse("""<h1>hi nikhil with h1</h1>
		<hr>
		<p>hello nkhil</p>

		""")


def home_with_html_file(request):
	return render(request, "home.html")	

def about(request):
	return render(request, "about.html", context={"peoples":peoples,'page':'about'})	

def contact(request):
	return render(request, "contact.html", context={"peoples":peoples,'page':'contact'})	

def career(request):
	return render(request, "career.html", context={"peoples":peoples,'page':'career'})		




def send_data_to_html(request):
	return render(request,"home.html",context={"peoples":peoples})

