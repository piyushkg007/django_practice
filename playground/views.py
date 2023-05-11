from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
   return render(request,"hello.html")
def say_hell(request):
   return render(request,"index.html")
def say_hell1(request):
   return render(request,"login.html")

