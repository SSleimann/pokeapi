from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

from apps.core.models import Pokemon, PokeType

class PokeTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokeType
        fields = ('name', 'description')

class PokemonModelSerializer(serializers.ModelSerializer):
    
    #type = PokeTypeModelSerializer(many=True)
    type = serializers.PrimaryKeyRelatedField(many=True, queryset=PokeType.objects.all())
    
    def validate(self, attrs):
        types = attrs.get('type')
        
        if len(types) > 2:
            raise ValidationError('Too many types!')
        
        return attrs
        
    class Meta:
        model = Pokemon
        fields = ('name', 'description', 'type', 'height', 'weight', 'picture')
    