from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.
from .models import Contact
from django.contrib import messages
from blog. models import Post

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
        messages.success(request, 'Feedback Sent!!!')
    return render(request,"home/contact.html")      

def about(request):
    return render(request,"home/about.html")      


def search(request):
    
    query=request.GET.get('search','')
    if(len(query)>80):
        allPosts=[]
    else:
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsCategory = Post.objects.filter(category__icontains=query)
        allPosts= allPostsTitle.union(allPostsContent,allPostsCategory)
    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)