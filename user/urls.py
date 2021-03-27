from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.user, name="userPage"),
    path('user/login', views.login, name="login"),
    path('user/register', views.register, name="register")
]
