from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings

from apps.accounts.serializers.profileserializer import ProfileModelSerializer
from apps.core.models import User, Profile
from apps.accounts.utils import send_user_verify_email

from knox.auth import AuthToken

import jwt

class UserModelSerializer(serializers.ModelSerializer):
    
    profile = ProfileModelSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile'
        )
        read_only_fields = ('email',)
    

class UserSingUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, 
        max_length=64,
        trim_whitespace=False,
        write_only=True
    )
    
    password_confirmation = serializers.CharField(
        min_length=8, 
        max_length=64,
        trim_whitespace=False,
        write_only=True
    )
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password_confirmation'
        )
    
    def validate(self, attrs):
        password = attrs.get('password')
        password_conf = attrs.get('password_confirmation')
        
        if password != password_conf:
            raise ValidationError(_("Passwords don't match."))
        
        validate_password(password)
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        
        user = User.objects.create_user(**validated_data, is_verified=False)
        Profile.objects.create(user=user)
        
        send_user_verify_email(user.pk)
        
        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    password = serializers.CharField(
        min_length=8, 
        max_length=64,
        trim_whitespace=False,
        write_only=True
    )
    
    def validate(self, attrs):   
        email = attrs.get('email')
        passwd = attrs.get('password')
        request = self.context.get('request')
        
        user = authenticate(request, username=email, password=passwd)
        
        if not user:
            raise ValidationError(_("Invalid credentials!"))
        
        if not user.is_verified:
            raise ValidationError(_("You are not verified!"))
        
        self.context['user'] = user
        
        return attrs
    
    def create(self, data):
        user = self.context.get('user')
        
        instance, token = AuthToken.objects.create(user=user)
        
        token_data = {
            'token': token,
            'expiry': instance.expiry
        }
        
        return user, token_data
    

class TokenVerificationSerializer(serializers.Serializer):
    token = serializers.CharField()
    
    def validate_token(self, data):
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms="HS256")
        except (jwt.PyJWTError):
            raise serializers.ValidationError(_('Invalid token!'))
        
        if payload['type'] != '_email_confirmation':
            raise serializers.ValidationError(_('Invalid token!'))
        
        self.context['payload'] = payload
        
        return data
    
    def save(self, **kwargs):
        payload = self.context['payload']
        user = get_user_model().objects.get(username=payload['user'])
        user.is_verified = True
        
        user.save()
        return user
    
