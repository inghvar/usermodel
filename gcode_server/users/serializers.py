from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import CustomUser


class UserLoginSerializer(serializers.Serializer):
    """autorusation"""
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):

    # company = CompanySerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone')


class UserCreateSerializer(serializers.ModelSerializer):
    """Create User"""
    # company = CompanySerializer(required=False)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user
        
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    class Meta:
        model = CustomUser
        fields = ('id',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'phone')
