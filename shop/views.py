from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.


@login_required(login_url='login')
def shop(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product.html', {'product': product})
