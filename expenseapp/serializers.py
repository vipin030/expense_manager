from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
    	instance = User.objects.create_user(**validated_data)
    	return instance

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
