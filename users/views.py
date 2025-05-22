from django.shortcuts import render
from rest_framework.decorators import api_view
from users.serializers import UserCreateSerializer, UserAuthorizationSerializer, UserRegistrationSerializer
from users.models import UserConfirmation
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView



class UserCreateAPIView(APIView):
    def post(self, request):

        # step 1: validation
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # step 2: receive data
        username = serializer.validated_data.get['username']
        password = serializer.validated_data.get['password']
        # step 3: create user
        user = User.objects.create_user(username=username, password=password)

        # step 4: return response
        
        return Response(status=status.HTTP_201_CREATED, 
                        data={'user_id': user.id,})


 
class AuthAPIView(APIView):
    def post(self, request):
        # step 1: validation
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        confirmation_code = serializer.validated_data.get('confirmation_code')

        # step 2: authentication
        try:
            confirmation = UserConfirmation.objects.get(
                confirmation_code=confirmation_code,)
            user = confirmation.user
            user.is_active = True
            user.save()
            confirmation.delete()
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key}, status=status.HTTP_201_CREATED)
        except UserConfirmation.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST,)
        


# Create your views here.
