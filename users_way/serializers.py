from rest_framework import serializers
from .models import SynergyUser, SynergyGroup


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SynergyUser
        fields = (
            'id', 'username', 'password', 'synergy_group', 'date_joined'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = SynergyUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SynergyGroup
        fields = (
            'id', 'title', 'description'
        )
