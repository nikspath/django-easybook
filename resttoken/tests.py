from django.test import TestCase

# Create your tests here.
import requests
import json

def test_signup():
	url="http://127.0.0.1:8000/resttoken/signup/"
	headers={"contentType":"application/json"}
	body={
		"phone_number":"9870888645",
		"password":"abc11",
		"email":"abc11@g.com",
		"is_superuser":True,
		"is_staff":True,
		"is_active":True
		}

	response=requests.post(url,json=body,headers=headers)
	print("signup response ", response.json())
	#signup response  {'toekn': '8e76407c09dd40d8d2615cba5ea4fd6b9c90697a', 'message': 'User created'}
	#signup response  {'toekn': '47193021fb31d6d7fde416d42468b4651ea982c8', 'message': 'User created'}

def test_login():
	url="http://127.0.0.1:8000/resttoken/login/"
	headers={"contentType":"application/json"}
	body={
		"phone_number":"9870888649",
		"password":"1234",
		}

	response=requests.post(url,json=body,headers=headers)
	print("login response ", response.json())
	#login response  {'token': '47193021fb31d6d7fde416d42468b4651ea982c8', 'message': 'login sucess'}

def test_token():
	url="http://127.0.0.1:8000/resttoken/example_view/"
	headers={
	"contentType":"application/json",
	"Authorization":'Token 005b7d11f666dc2efa02db5d063208f13a657df4'
	}
	response=requests.get(url,headers=headers)
	print(response.json())
	# curl -X GET http://127.0.0.1:8000/resttoken/example_view/  -H "Authorization: Token 005b7d11f666dc2efa02db5d063208f13a657df4"



if __name__ == '__main__':
	#test_signup()
	#test_login()
	test_token()
