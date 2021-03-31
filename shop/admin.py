from django.contrib import admin

# Register your models here.
from .models import Product, Deal


admin.site.register(Product)
admin.site.register(Deal)
