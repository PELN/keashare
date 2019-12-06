from rest_framework import serializers
from keashareapp.models import AppGroup

# Group serializer
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = ('id', 'owner', 'name', 'description')

