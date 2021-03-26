from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="homePage"),
    path('contact/', views.contact, name="contact"),
    path('home/', views.home, name="home"),
]
