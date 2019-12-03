from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest

def index(request):
    return render(request, 'keashareapp/index.html')


# def profile(request):
#     return render(request, 'keashareapp/profile.html')


