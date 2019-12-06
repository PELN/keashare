from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from .utils import random_string
from .models import *
from django.contrib.auth.decorators import login_required

from .tasks import add
# from .tasks import sendEmail

def login(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(request,
            username=request.POST['user'], 
            password=request.POST['password'])
        if user:
            dj_login(request, user)
            # return HttpResponseRedirect(reverse ('keashareapp:index'))
            return HttpResponseRedirect(reverse ('keashareapp:index'))
        else:
            context['error'] = "Username or password is wrong."

    return render(request, 'loginapp/login.html', context)


def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse ('loginapp:login'))


def register(request):
    if User.is_authenticated:
        dj_logout(request)

    if request.method == 'POST':
        context = {}
        if not request.POST['password'] == request.POST['confirmPassword']:
            context['error'] = "Passwords do not match."
            return render(request, 'loginapp/register.html', context)
        #check if the list of users is empty or not - use len
        if len(User.objects.filter(username = request.POST['user'])) > 0:
            context['error'] = 'Username already exists'
            return render(request, 'loginapp/register.html', context)

        # create user
        user = User.objects.create_user(request.POST['user'],password=request.POST['password'],email=request.POST['email'])
        user.save()
        dj_login(request, user)
        # return HttpResponseRedirect(reverse ('keashareapp:index'))
        return HttpResponseRedirect(reverse ('loginapp:profile'))
    
    return render(request, 'loginapp/register.html')


def reset_password(request):
    context = {}
    if request.method == 'POST':
        users = User.objects.filter(username=request.POST['user']) # use filter to check list of users contain username
        if users: # if user exists, generate random string for new password, show in console
            user = users[0]
            new_password = random_string()
            user.set_password(new_password)
            user.save()
            print(f'*********** User {user} change password to {new_password}')
            return HttpResponseRedirect(reverse('loginapp:login'))
        else:
            context['error'] = "No such username"

    return render(request, 'loginapp/reset_password.html', context)


def sendemail(request):
    add.delay(5, 5)
    # sendEmail.delay()
    return HttpResponse('<h1>Task is done!!!</h1>')
    # return render(request, 'loginapp/sendemail.html')


def profile(request):
    return render(request, 'loginapp/profile.html')


def edit_profile(request):
    if request.method == 'GET':
        profile_info = Profile.objects.filter(user=request.user)
      
        context = {
            'profile': profile_info
        }
        return render(request, 'loginapp/edit_profile.html', context)

    if request.method == 'POST':
        # profile_info = Profile() # makes a new profile object for every post (only use for items)
        profile_info = Profile.objects.get(user=request.user) # get the user in db

        # print("request.user")
        profile_info.bio = request.POST.get('bio')
        profile_info.city = request.POST.get('city')
        profile_info.study = request.POST.get('study')
        profile_info.user = request.user
        profile_info.save()
        return HttpResponseRedirect(reverse ('loginapp:profile'))
    
    return HttpResponseBadRequest()

