from django.http import HttpResponse
from django.shortcuts import render
def register(request):
    return render(request,"register.html")

def about(request):
    return render(request,"about.html")

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")