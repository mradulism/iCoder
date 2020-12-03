from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("you are in home")

def blog(request):
    return HttpResponse("you are in blog")