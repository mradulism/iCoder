from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.
from .models import Contact

def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        content=request.POST.get('content','')

        ContactObj=Contact(name=name,email=email,phone=phone,content=content)
        ContactObj.save()
    return render(request,"home/contact.html")      

def about(request):
    

    return render(request,"home/about.html")      
