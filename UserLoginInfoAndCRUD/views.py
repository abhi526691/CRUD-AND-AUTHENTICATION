from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .forms import CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms1 import CreateProfile
from .models import Profile

def index(request):
    all_users= get_user_model().objects.all()
    context = {'all_users' : all_users}
    return render(request, 'index.html', context)

def ProfileCreation(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        # else:
        #     return render(request, 'profile.html', {'form':form})
    else:
        form = CreateProfile()
        context = {'form' : form}
        return render(request, 'profile.html', context)


def register(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('/')
        else:
            context = {'form' : form}
            return render(request, 'register.html', context)
    else:
        form = CreateUser()
        context = {'form' : form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('index')
        else:
            messages.info(request, 'Username and Password Not Matched')
    else:
        return render(request, 'login.html') 

def logoutPage(request):
    logout(request)
    return redirect('login')

def profileDetail(request):
    prof = Profile.objects.all()
    context = {'prof' : prof}
    return render(request, 'profileDetail.html', context) 

def detail(request, id):
    det = Profile.objects.get(id=id)
    form = CreateProfile(instance=det)
    if request.method == 'POST':
        form = CreateProfile(request.POST, request.FILES, instance=det)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        context = {'form' : form, 'det' : det}
        return render(request, 'detail.html', context)




           
        



