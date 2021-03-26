from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def user(request):
    return HttpResponse("<h1> hello <h1/>")

def login(request):
    return render(request, "user/login.html")
