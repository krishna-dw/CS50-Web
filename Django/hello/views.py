from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def krishna(request):
    return HttpResponse("Hello, Krishna!")

def dewabrata(request):
    return HttpResponse("Hello, Dewabrata!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })