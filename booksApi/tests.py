from django.test import TestCase

# Create your tests here.
import requests

url="http://127.0.0.1:8000/booksapi/update_book/"
body={
	"book_id":3,
	 "name": "godzilla",
     "rating": 10,
     "is_published": False
}
request=requests.put(url,body)
print(request.json())