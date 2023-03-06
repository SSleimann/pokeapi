from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.core.models import Profile

# Create your tests here.
class TestUsers(TestCase):
    def test_create_user(self):
        password = 'pruebapassword'
        
        user = get_user_model().objects.create_user(
            username='prueba',
            email='prueba@prueba.com',
            password=password,
            first_name='pruebita',
            last_name='pruebona'
        )
        
        finded_user = get_user_model().objects.filter(email='prueba@prueba.com')
        
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_verified)
        self.assertTrue(user.check_password(password))
        self.assertTrue(finded_user.exists())
        self.assertFalse(user.is_staff)
    
    def test_create_superuser(self):
        password = 'pruebapassword'
        
        user = get_user_model().objects.create_superuser(
            username='prueba',
            email='prueba@prueba.com',
            password=password,
            first_name='pruebita',
            last_name='pruebona'
        )
        
        finded_user = get_user_model().objects.filter(email='prueba@prueba.com')
        
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_verified)
        self.assertTrue(user.check_password(password))
        self.assertTrue(finded_user.exists())
        self.assertTrue(user.is_staff)
    
    def test_create_profile(self):
        user = get_user_model().objects.create_superuser(
            username='prueba',
            email='prueba@prueba.com',
            password='pruebaPassword',
            first_name='pruebita',
            last_name='pruebona'
        )
        profile = Profile.objects.create(user=user)
        
        finded_profile = Profile.objects.filter(user__email='prueba@prueba.com')
        
        self.assertEqual(str(profile), str(user))
        self.assertTrue(finded_profile.exists())
    
