from django.test import TestCase

from apps.core.models import PokeType, Pokemon

# Create your tests here.
class TestsPoke(TestCase):
    def test_create_pokemon_type(self):
        PokeType.objects.create(name='Aqua')
        PokeType.objects.create(name='Electric')
        PokeType.objects.create(name='Fire')
        
        self.assertTrue(PokeType.objects.filter(name='Aqua').exists())
        self.assertTrue(PokeType.objects.filter(name='Electric').exists())
        self.assertTrue(PokeType.objects.filter(name='Fire').exists())
    
    def test_create_pokemon(self):
        type1 = PokeType.objects.create(name='Electric')
        type2 = PokeType.objects.create(name='Test')
        
        poke = Pokemon.objects.create(
            name='Pikachu',
            height=250,
            weight=1000
        )
        poke.type.add(type1, type2)
        
        self.assertTrue(Pokemon.objects.filter(name='Pikachu').exists())
        self.assertEqual(poke.type.all().count(), 2)
        self.assertIn(type1, poke.type.all())
        self.assertIn(type2, poke.type.all())
        
