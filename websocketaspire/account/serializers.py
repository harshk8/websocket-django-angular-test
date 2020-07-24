from rest_framework import routers, serializers, viewsets
from rest_framework.validators import UniqueValidator, ValidationError
from rest_framework import status

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class SignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        max_length=50,

        )
    password = serializers.CharField(
        required=True,
        max_length=50,
        )
    confirm_password = serializers.CharField(
        required=True,
        max_length=50,
        )

    def validate(self, validated_data):
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']

        if len(password) < 8:

        	raise ValidationError(
        		'Password should be 8 char alpha-neumeric.')

        if password != confirm_password:

        	raise ValidationError(
        		'Password & confirm password must be same.')

        return validated_data


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True,
        required=True,
        help_text='Write altest 8 character alpha-neumeric password',
        )

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        try:
            user = User.objects.get(username=username)

        except:
            raise ValidationError('Given credentials are not correct.')

        if not user.check_password(password):

            raise ValidationError('Given credentials are not correct.')

        return validated_data


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, validated_data):
        user = self.context['request'].user

        if not user.check_password(validated_data['password']):

            raise ValidationError('Existing password not correct.')

        if len(validated_data['new_password']) < 8:

            raise ValidationError(
            	'New password should be 8 char alpha-neumeric.')

        return validated_data