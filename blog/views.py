from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.
def blogHome(request):
    return HttpResponse("This is blog home")

def blogPost(request,slug):
    return HttpResponse(f"you are in blogPost:{slug}")      