from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from accounts.models import CustomeUser, Profail


class RegisterationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = CustomeUser
        fields = ["email", "username", "password", "password1"]

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password")

        if password1 != password2:
            raise serializers.ValidationError({"detail": "password dose not confirmed"})

        try:

            validate_password(password1)

        except exceptions.ValidationError as e:

            raise serializers.ValidationError({"detail": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return CustomeUser.objects.create_user(**validated_data)


class  ResendEmailSerializer(serializers.Serializer):
     
    email = serializers.CharField(label = ("Email"), write_only=True)
     
    def validate(self, attrs):

        user = get_object_or_404(CustomeUser,email = attrs.get("email"))
        attrs["user"] = user
        return attrs