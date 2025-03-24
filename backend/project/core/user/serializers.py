from rest_framework import serializers
from core.user.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, source='public_id', format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'created', 'updated', 'bio', 'avatar', 'is_active')
        read_only_fields = ['is_active']



    
                            