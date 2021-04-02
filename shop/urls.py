from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('shop/', views.shop, name="shopPage"),
    path('product/<int:product_id>', views.product, name="product"),
    path('deals/', views.addDeals, name="deals"),
    path('save/<int:product_id>', views.saveDeal, name="saveDeal")
]
