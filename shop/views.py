from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product, Deal
from .forms import dealsForm
from django.utils import timezone
# Create your views here.


def shop(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'shop/index.html', context)


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product.html', {'product': product})


def addDeals(request):
    f = dealsForm()
    return render(request, 'shop/product.html', {'f': f})


@login_required(login_url='login')
def saveDeal(request, product_id):
    if request.method == 'POST':
        user = request.user
        product = Product.objects.get(id=product_id)
        date_posted = timezone.now()
        size = request.POST['size']
        quantity = request.POST['quantity']
        ins = Deal(user=user, product=product, date_posted=date_posted,
                   size=size, quantity=quantity)
        ins.save()
        return redirect('shopPage')
    else:
        return redirect('product')


@login_required(login_url='login')
def seenDeal(request):
    query = Deal.objects.filter(user=request.user)
    content = {
        "object_deal": query
    }
    return render(request, 'shop/deals.html', content)
