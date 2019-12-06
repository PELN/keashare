from django.shortcuts import render

from keashareapp.models import AppGroup
from rest_framework import viewsets, permissions
from .serializers import GroupSerializer


# Group Viewset
class GroupViewSet(viewsets.ModelViewSet):
    queryset = AppGroup.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer


