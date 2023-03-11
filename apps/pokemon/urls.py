from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.pokemon.views import PokemonViewSet

app_name = 'pokemon'

router = DefaultRouter()
router.register('', PokemonViewSet, 'poke')

urlpatterns = [
    path('', include(router.urls)),
]
