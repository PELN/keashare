from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from . import models

def index(request):
    user = request.user
    if request.method == 'GET':
        user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
        posts = models.Post.objects.filter(group__in=user_groups).order_by('-created')[:10] # show correct posts, order-by, limit

        context = {
            'user': user,
            'posts': posts,
            'user_groups': user_groups
        }

        return render(request, 'keashareapp/index.html', context=context)

def groups(request):
    user = request.user

    # get list of groups user is/is not member
    if request.method == 'GET':
        user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
        not_user_groups = models.AppGroup.objects.exclude(users__username__contains=user.username)

        context = {
            'user': user, # the user who is logged in
            'user_groups': user_groups,
            'not_user_groups': not_user_groups,
        }
        return render(request, 'keashareapp/groups.html', context=context)

    # create group
    if request.method == 'POST':
        group = models.AppGroup()
        group.name = request.POST['name']
        group.description = request.POST['description']
        group.owner = user
        group.save() # it needs to be saved first to have a primary key
        group.users.add(user)
        group.save() # then save it again with the user
        return HttpResponseRedirect(reverse('keashareapp:groups'))

    return HttpResponseBadRequest() # if it is neither post or get


def groupdetails(request, pk):
    user = request.user

    if request.method == 'GET':
        # get the group that is clicked on (pk)        
        user_groups = models.AppGroup.objects.filter(pk=pk)
        group_pk = models.AppGroup.objects.get(pk=pk)

        # filter posts based on the group pk
        posts = models.Post.objects.filter(group__in=user_groups).order_by('-created')

        context = {
            'user': user,
            'posts': posts,
            'user_groups': user_groups,
            'group_pk': group_pk,
        }
        return render(request, 'keashareapp/groupdetails.html', context=context)
    
    if request.method == 'POST':
        post = models.Post()
        post.text = request.POST['text']
        post.group = models.AppGroup.objects.get(pk=request.POST['group'])
        post.user = user
        post.save()
        return HttpResponseRedirect(reverse('keashareapp:post_submit')) # post_submit url -> post_submit view

    return HttpResponseBadRequest()

def post_submit(request):
    # redirect to previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def join_group(request, pk):
    user = request.user
    group = models.AppGroup.objects.get(pk=pk)
    group.users.add(user)
    group.save()
    return HttpResponseRedirect(reverse('keashareapp:groups'))


def leave_group(request, pk):
    user = request.user
    group = models.AppGroup.objects.get(pk=pk)
    group.users.remove(user)
    group.save()
    return HttpResponseRedirect(reverse('keashareapp:groups'))


