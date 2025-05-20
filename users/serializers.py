from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import UserConfirmation
from django.contrib.auth.models import User
import random



def generate_confirmation_code():
    return str(random.randint(100000, 999999))


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'confirmation_code']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.save()

        confirmation_code = generate_confirmation_code()
        UserConfirmation.objects.create(
            user=user,
            confirmation_code=confirmation_code
        )
        return user


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("Пользователь с таким именем уже существует!")


class UserAuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

