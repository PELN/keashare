from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'keashareapp/index.html')

@login_required
def groups(request):



    return render(request, 'keashareapp/groups.html')



@login_required
def groupdetails(request):
    pass

@login_required
def join_group(request):
    pass

@login_required
def leave_group(request):
    pass



