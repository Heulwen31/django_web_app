from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return response with template and context 
    return render(request, "home/index.html") 


def contact(request):
    return render(request, "home/contact.html")