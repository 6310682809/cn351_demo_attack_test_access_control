from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from post.models import Post
from django.contrib.auth.models import User
from user.models import UserInfo

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user:signin'))
    all_post = Post.objects.all().order_by("-created_at")

    return render(request, 'post/post.html',
            {
                'all_post': all_post,
            })

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/view_post.html',
            {
                'post': post,
            })

def create_post(request):
    if request.method == "POST":
        detail = request.POST["detail"]

        user = User.objects.get(username=request.user.username)
        userInfo = UserInfo.objects.get(user_id=user)
        Post.objects.create(created_by=userInfo, detail=detail)

    return HttpResponseRedirect(reverse('post:index'))

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        detail = request.POST["detail"]
        post.detail = detail
        post.save()

        return HttpResponseRedirect(reverse('post:index'))
    return render(request, 'post/edit_post.html',
            {
                'post': post,
            })

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return HttpResponseRedirect(reverse('post:index'))