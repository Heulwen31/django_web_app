from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('shop/', views.shop, name="shopPage"),
<<<<<<< HEAD
    path('product/<int:product_id>', views.product, name="product"),
=======
    path('product/', views.product, name="product"),
>>>>>>> e7ad210fe9de3e17f6030a6611c6438f9c547aef
]
