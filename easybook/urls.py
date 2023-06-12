"""
URL configuration for easybook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from vegan.views import *
from accounts.views import *
from students.views import *


urlpatterns = [
    path("resttoken/",include('resttoken.urls')),
    path("booksapi/",include('booksApi.urls')),
    path("",home, name="home"),
    path("login/",login_page, name="login"),
    path("register/",register_page, name="register"),
    path("logout/",logout_page, name="register"),
    path("receipe_form/",receipe_form, name="receipe_form"),
    path("students/",student_report,name="student_report"),
    path("student_detail/<std_id>", student_detail, name="student_detail"),
    path("receipe/",receipe, name="receipe"),
    path("homewithhH1/", homewithhH1, name='homewithhH1'),
    path("about/", about, name='about'),
    path("delete-receipe/<id>", delete_receipe, name="delete_receipe"),
    path("update-receipe/<id>", update_receipe, name="update_receipe"),
    path("contact/", contact, name='contact'),
    path("career/", career, name='career'),
    path("home_with_html_file/", home_with_html_file, name="home_with_html_file"),
    path("send_data_to_html/",send_data_to_html, name="send_data_to_html"),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
