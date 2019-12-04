from django.urls import path
from . import views

app_name = 'keashareapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
    path('join_group/<int:pk>', views.join_group, name='join_group'),
    path('leave_group/<int:pk>', views.leave_group, name='leave_group'),
    path('groupdetails/<int:pk>', views.groupdetails, name='groupdetails'),
    path('post_submit/', views.post_submit, name='post_submit'),
    # path('post_submit_back/<int:pk>', views.post_submit_back, name='post_submit_back')
]



