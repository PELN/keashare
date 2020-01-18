from rest_framework import serializers
from keashareapp.models import AppGroup

# Convert model instance to JSON
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = ('id', 'owner', 'name', 'description')
