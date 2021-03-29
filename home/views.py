from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return response with template and context 
    return render(request, "home/index.html") 


def contact(request):
    return render(request, "home/contact.html")


def story(request):
    return render(request, "home/story.html")


def journal(request):
    return render(request, "home/journal.html")

def journal1(request):
    return render(request, "home/journal1.html")

def journal2(request):
    return render(request, "home/journal2.html")