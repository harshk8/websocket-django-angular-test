from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password

from .serializers import SignUpSerializer, LoginSerializer, UserSerializer, ChangePasswordSerializer


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data.pop('confirm_password')
        data['password'] = make_password(data['password'])

        user = User.objects.create(**data)
        token = Token.objects.create(user=user)

        return Response(data={
            'message': 'Account successfully created',
            'token': token.key,
            'username': user.username,
            'id': user.id,
            'status': True
            },
            status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)

            if not user:

                return Response(data={
                    'message': 'Given credentials are not correct.',
                    'status': False
                    }, status=status.HTTP_400_BAD_REQUEST)

            token, created = Token.objects.get_or_create(user=user)

            return Response(data={
                'id': user.id,
                'token': token.key,
                'status': True,
                'username': user.username,
                }, status=status.HTTP_200_OK
            )

        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        user = self.request.user
        serializer = self.serializer_class(data=request.data,
            context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data['new_password'])
        user.save()

        return Response(data={
            'message':'Password successfully update',
            'status': True
            }, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permissions_classes = (IsAuthenticated,)
    
    def post(self, request):
        Token.objects.get(user=self.request.user).delete()

        return Response(data={
            'message': 'User successfully logged out',
            'status': True
            }, status=status.HTTP_200_OK)


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permissions_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = User.objects.filter(user_id=self.request.user.user_id)
        return user

    def update(self, request, pk=None):
        serializer = self.serializer_class(
            data=request.data, instance=self.request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={
            'data': serializer.data,
            'status': True
            }, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = self.serializer_class(
            data=request.data, instance=self.request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={
            'data': serializer.data,
            'status': True
            }, status=status.HTTP_200_OK)