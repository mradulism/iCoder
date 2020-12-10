from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.blogHome,name="blogHome"),
    # API to post comment
    path('postComment',views.postComment,name="postComment"),
    path('<str:slug>', views.blogPost,name="blogPost"),
]
#hello
