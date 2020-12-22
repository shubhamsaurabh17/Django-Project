from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=False,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
