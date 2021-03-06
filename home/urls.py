from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="homePage"),
    path('contact/', views.contact, name="contact"),
    path('home/', views.home, name="home"),
    path('story/', views.story, name="story"),
    path('journal/', views.journal, name="journal"),
    path('journal1/', views.journal1, name="journal1"),
    path('journal2/', views.journal2, name="journal2"),
]
