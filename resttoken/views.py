from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
# Create your views here.

@api_view(['POST'])
def test_login(request):
	phone_number=request.data.get('phone_number')
	password=request.data.get('password')
	user=get_object_or_404(User,phone_number = phone_number)
	if not user:
		return Response({"message":"user not found"})
	check_password=user.check_password(password)
	if not check_password:
		return Response({"message":"password not found"})
	token,created=Token.objects.get_or_create(user=user)
	print("token",token.key)
	return Response({"token":token.key,"message":"login sucess"}) 	


@api_view(['POST'])
def signup(request):
	phone_number=request.data.get('phone_number')
	password=request.data.get('password')
	email=request.data.get('email')
	user=User.objects.create(phone_number=phone_number,password=password,email=email)
	if user:
		user.set_password(password)
		user.save()
		token=Token.objects.create(user=user)
		return Response({'toekn':token.key, 'message':'User created'})
	else:
		return Response({'message':'User failed created'})	


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
	print("request",request)
	content = {
    	'user': str(request.user),  # `django.contrib.auth.User` instance.
    	'auth': str(request.auth),  # None
	}
	return Response(content)		


