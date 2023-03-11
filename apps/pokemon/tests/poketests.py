from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import exceptions
from rest_framework import status
from rest_framework.test import APIClient

from knox.auth import AuthToken

from apps.core.models import Pokemon, PokeType
from apps.pokemon.serializers.pokeserializers import PokemonModelSerializer, PokeTypeModelSerializer

# Create your tests here.
class PokemonTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = get_user_model().objects.create_superuser(
            username='prueba',
            email='prueba@prueba.com',
            password='megahyperpass12345',
            first_name='pruebita',
            last_name='pruebona'
        )
        
        instance, token = AuthToken.objects.create(user=user)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    
    def test_create_type(self):
        path = reverse_lazy('pokemon:poke-create-type')
        
        payload = {
            'name': 'Electric',
            'description': 'Elezzzz'
        }
        
        req = self.client.post(path, payload)
        
        poke_type = PokeType.objects.filter(name='Electric').exists()
        
        self.assertEqual(req.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(payload, req.data)
        self.assertTrue(poke_type)
    
    def test_create_invalid_type(self):
        path = reverse_lazy('pokemon:poke-create-type')
        
        payload = {
            'name': '',
            'description': 'Elezzzz'
        }
        
        req = self.client.post(path, payload)
        
        poke_type = PokeType.objects.filter(name='Electric').exists()
        
        self.assertEqual(req.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(poke_type)
    
    def test_all_types(self):
        path = reverse_lazy('pokemon:poke-all-types')
        
        PokeType.objects.create(name='TypeTestName1', description='desc')
        PokeType.objects.create(name='TypeTestName2', description='desc')
        PokeType.objects.create(name='TypeTestName3', description='desc')
        
        poke_types = PokeType.objects.all()
        
        poke_data = PokeTypeModelSerializer(poke_types, many=True).data
        
        req = self.client.get(path)
        
        self.assertEqual(req.status_code, status.HTTP_200_OK)
        self.assertEqual(poke_data, req.data)
    
    def test_create_poke(self):
        path = reverse_lazy('pokemon:poke-create-poke')
        
        poke_type = PokeType.objects.create(name='Electric', description='desc').pk
        
        payload = {
            'name': 'Pikachu',
            'description': 'desc',
            'type': poke_type,
            'height': 100,
            'weight': 100
        }
        
        req = self.client.post(path, payload)
        
        pokemon = Pokemon.objects.filter(name='Pikachu')
        data = PokemonModelSerializer(pokemon.first()).data
        
        self.assertTrue(pokemon.exists())
        self.assertEqual(status.HTTP_201_CREATED, req.status_code)
        self.assertDictEqual(req.data, data)
    
    def test_create_poke_with_many_types(self):
        path = reverse_lazy('pokemon:poke-create-poke')
        
        PokeType.objects.create(name='Electric', description='desc')
        PokeType.objects.create(name='Dragon', description='desc')
        
        poke_types = PokeType.objects.all()
        
        payload = {
            'name': 'Pikachu',
            'description': 'desc',
            'type': [type.pk for type in poke_types],
            'height': 100,
            'weight': 100
        }
        
        req = self.client.post(path, payload)
        
        pokemon = Pokemon.objects.filter(name='Pikachu')
        data = PokemonModelSerializer(pokemon.first()).data
        
        self.assertTrue(pokemon.exists())
        self.assertEqual(status.HTTP_201_CREATED, req.status_code)
        self.assertDictEqual(req.data, data)
