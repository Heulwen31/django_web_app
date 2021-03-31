from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('shop/', views.shop, name="shopPage"),
    path('product/', views.product, name="product"),
]
