from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

def login_page(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		users=User.objects.filter(username=username)
		if not users.exists():
			messages.warning(request,"user invalid")
			return redirect('/login/')
		user=authenticate(username=username,password=password)
		if not user:
			messages.warning(request,"invalid password")
		else:
			login(request, user)
			return redirect('/receipe/')		
	return render(request, "login.html")	


def register_page(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		users=User.objects.filter(username=username)
		if users.exists():
			messages.warning(request,"user already exist")
			return redirect('/register/')
		user=User.objects.create(username=username)
		user.set_password(password)
		user.save()
		messages.success(request,"User added success")
		return redirect('/register/')
	return render(request, "register.html")	


def logout_page(request):
	logout(request)
	return redirect("/login/")		