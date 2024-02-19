from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from userprofiles.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = (
            make_password(validated_data['password'])
        )
        return super().create(validated_data)

    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['owner']
