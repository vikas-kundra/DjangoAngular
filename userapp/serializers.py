from .models import User_new, User
from rest_framework import serializers

class User_new_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_new
        fields = ('user_name','age','country')


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class test_serializer(serializers.Serializer):
    email = serializers.EmailField()







