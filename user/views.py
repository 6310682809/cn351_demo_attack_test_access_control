from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user.models import UserInfo

# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('post:index'))
        else:
            return render(request, 'user/signin.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'user/signin.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        cpassword = request.POST["password confirmation"]
        email = request.POST["email"]
        role = request.POST["role"]

        user = User.objects.create_user(username, email, password)

        UserInfo.objects.create(user=user, role=role)

        return render(request, 'user/signin.html')
    return render(request, 'user/signup.html')

def signout(request):
    logout(request)
    return render(request, 'user/signin.html', {
        'message': 'Logged out'
    })