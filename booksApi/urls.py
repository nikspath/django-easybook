from django.urls import path
from .views import * 

urlpatterns = [
path("",books, name="books_api"),
path("all_books/", all_books, name="books_apiapi"),
path("create_books/", create_books, name="create_books"),
path("delete_books/",delete_books, name="delete_books"),
path("update_book/", update_book , name="update_book"),
]