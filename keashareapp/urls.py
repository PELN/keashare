from django.urls import path
from . import views

app_name = 'keashareapp'

urlpatterns = [
    path('', views.index, name='index'),
]



