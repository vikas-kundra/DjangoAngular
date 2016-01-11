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
    joined = serializers.DateTimeField()
    age = serializers.IntegerField()
    country = serializers.CharField()


class insert_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','name','age','country','password')

    def create(self, validated_data):
        print 'Object getting created now'
        print validated_data

        user = User.objects.create(**validated_data)
        print 'Obtaining password'
        user.set_password(validated_data.get('password'))
        user.save()
        return user