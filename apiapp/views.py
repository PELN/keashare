from keashareapp.models import AppGroup
from rest_framework import viewsets, permissions
from .serializers import GroupSerializer

# Create ViewSet on Model
class GroupViewSet(viewsets.ModelViewSet):
    queryset = AppGroup.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer
