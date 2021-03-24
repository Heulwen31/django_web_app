from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    context ={ 
        "data":"Gfg is the best", 
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    } 
    # return response with template and context 
    return render(request, "home/index.html", context) 
