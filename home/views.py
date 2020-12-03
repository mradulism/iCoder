from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("you are in home")

def contact(request):
    return HttpResponse("you are in contact")      

def about(request):
    return HttpResponse("you are in about")      
