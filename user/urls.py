from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('user/login/', views.logIn, name="login"),
    path('user/logout/', views.logOut, name="logout"),
    path('user/register/', views.register, name="register"),
]
