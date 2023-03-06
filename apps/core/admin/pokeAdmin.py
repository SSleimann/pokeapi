from django.contrib import admin

from apps.core.models import PokeType, Pokemon

class PokeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
        'height',
        'weight',
    )
    raw_id_fields = ('type',)
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(PokeType, PokeTypeAdmin)
admin.site.register(Pokemon, PokemonAdmin)