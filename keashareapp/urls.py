from django.urls import path
from . import views

app_name = 'keashareapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
    path('join_group/<int:pk>', views.join_group, name='join_group'),
    path('leave_group/<int:pk>', views.leave_group, name='leave_group'),
    path('groupdetails/<int:pk>', views.groupdetails, name='groupdetails'),
]



