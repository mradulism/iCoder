from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from blog.models import Post,BlogComment
from django.contrib import messages

# Create your views here.

def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,"blog/blogHome.html",context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    
    # getting comment for above post
    comments=BlogComment.objects.filter(post=post)
    context={'post':post,'comments':comments}
    return render(request,"blog/blogPost.html",context)      

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)

        commentObj=BlogComment(comment=comment,user=user,post=post)
        commentObj.save()
        messages.success(request,'your comment has been posted')

    return redirect(f"/blog/{post.slug}")      