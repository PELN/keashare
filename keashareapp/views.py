from django.shortcuts import render


def index(request):
    return render(request, 'keashareapp/index.html')


def profile(request):
    return render(request, 'keashareapp/profile.html')


def edit_profile(request):
    pass