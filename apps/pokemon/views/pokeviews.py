from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from apps.pokemon.serializers import (
    PokeTypeModelSerializer,
    PokemonModelSerializer
)

from apps.core.models import Pokemon, PokeType

# Create your views here.
class PokemonViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Pokemon.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'name'
    
    def get_serializer_class(self):
        
        if self.action in ['create_poke', 'retrieve', 'update', 'partial_update']:
            return PokemonModelSerializer
        
        elif self.action in ['create_type', 'all_types']:
            return PokeTypeModelSerializer
        
        return PokemonModelSerializer
        
    @action(detail=False, methods=['post'])
    def create_poke(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        data = serializer.data
        
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def create_type(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        data = serializer.data
        
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def all_types(self, request):
        obj = PokeType.objects.all()
        
        serializer = PokeTypeModelSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
