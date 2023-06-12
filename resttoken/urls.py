from django.urls import path
from .views import *

urlpatterns = [
path("signup/",signup,name="signup"),
path("login/",test_login,name="test_login"),
path("example_view/", example_view, name="example_view"),
]
