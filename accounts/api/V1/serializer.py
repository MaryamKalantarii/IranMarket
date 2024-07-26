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


class ResendEmailSerializer(serializers.Serializer):
     
    email = serializers.CharField(label = ("Email"), write_only=True)
     
    def validate(self, attrs):

        user = get_object_or_404(CustomeUser,email = attrs.get("email"))
        attrs["user"] = user
        return attrs



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if not self.user.is_verified:
            msg = "your account is not verified"
            raise serializers.ValidationError(msg , code = "authorization")
        validated_data["id"] = self.user.id
        validated_data["email"] = self.user.email
        return validated_data


class PasswordChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField(max_length=20)
    new_password1 = serializers.CharField(max_length=20)
    new_password2 = serializers.CharField(max_length=20)

    def validate(self, attrs):
        pass1 = attrs.get("new_password1")
        pass2 = attrs.get("new_password2")

        if pass1 != pass2:
            raise serializers.ValidationError({"detail": "password dose not confirmed"})
        
        return super().validate(attrs)
    
    def check_old_password(self,request,attrs:dict):

        old_pass = attrs.get("old_password")
        pass1 = attrs.get("new_password1")
        user = request.user

        if not user.check_password(old_pass):
            raise serializers.ValidationError({"detail": "old password is not correct"})
        
        if old_pass == pass1:
            raise serializers.ValidationError({"detail": "old password and new password are same"})
        
        return attrs

    def set_new_password(self, request, attrs: dict):
        pass1 = attrs.get("new_password1")
        user = request.user

        try:
            validate_password(pass1)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})
            
        user.set_password(pass1)
        user.save()
        return attrs    

        
class ProfailSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length = 100 , source="user.email" , read_only=True)

    class Meta:
        model = Profail
        fields = ["email", "first_name", "last_name", "image", "phone", "address"]



class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)

    def validate(self, attrs):
        user = get_object_or_404(CustomeUser, email=attrs.get('email'))
        attrs['user'] = user
        return attrs


class ResetPasswordSerializer(serializers.Serializer):

    new_password1 = serializers.CharField(max_length=20)
    new_password2 = serializers.CharField(max_length=20)

    def validate(self, attrs):
        pass1 = attrs.get('new_password1')
        pass2 = attrs.get('new_password2')

        if pass1 != pass2:
            raise serializers.ValidationError({'detail': 'Passwords do not match'})

        return super().validate(attrs)

    def set_new_password(self, request, attrs:dict):
        pass1 = attrs.get("new_password1")
        user = request.user

        try:
            validate_password(pass1)

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})
        
        user.set_password(pass1)
        user.save()
        return attrs
    

