from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.accounts.serializers import (
    UserModelSerializer, 
    UserSingUpSerializer, 
    ProfileModelSerializer,
    UserLoginSerializer,
    TokenVerificationSerializer
)

from apps.accounts.permissions import IsOwnerPermission

# Create your views here.
class UserViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = get_user_model().objects.all()
    lookup_field = 'username'
        
    def get_serializer_class(self):
        if self.action == 'signup':
            return UserSingUpSerializer 
           
        elif self.action == 'profile':
            return ProfileModelSerializer
        
        elif self.action == 'login':
            return UserLoginSerializer
        
        elif self.action == 'verify':
            return TokenVerificationSerializer
        
        return UserModelSerializer
    
    def get_permissions(self):
        if self.action in ['login', 'signup', 'verify']:
            permissions = [AllowAny]
        
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsOwnerPermission]
        
        else:
            permissions = [IsAuthenticated]
        
        return [p() for p in permissions]
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        
        serializer = self.get_serializer(
            instance=profile,
            partial=partial,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def verify(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        data = {
            'user': user.username,
            'verified': user.is_verified
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
