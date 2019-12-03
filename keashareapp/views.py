from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models

@login_required
def index(request):
    return render(request, 'keashareapp/index.html')

@login_required
def groups(request):
    user = User.objects.filter(pk=1)[0]

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


@login_required
def posts(request):
    pass


@login_required
def groupdetails(request, pk):
    user = User.objects.filter(pk=1)[0]

    if request.method == 'GET':
        # get the group that is clicked on (pk)        
        user_groups = models.AppGroup.objects.filter(pk=pk)
        # filter posts based on the group pk
        posts = models.Post.objects.filter(group__in=user_groups).order_by('-created')

        context = {
            'user': user,
            'posts': posts,
            'user_groups': user_groups,
        }
        return render(request, 'keashareapp/groupdetails.html', context)
    return HttpResponseBadRequest()


@login_required
def join_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    group = models.AppGroup.objects.get(pk=pk)
    group.users.add(user)
    group.save()
    return HttpResponseRedirect(reverse('keashareapp:groups'))


@login_required
def leave_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    group = models.AppGroup.objects.get(pk=pk)
    group.users.remove(user)
    group.save()
    return HttpResponseRedirect(reverse('keashareapp:groups'))


