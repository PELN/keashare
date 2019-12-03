from django.urls import path
from . import views

app_name = 'loginapp'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password'),
]