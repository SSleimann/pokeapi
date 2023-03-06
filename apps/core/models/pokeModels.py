from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.utils import poke_directory_path

class PokeType(models.Model):
    name = models.CharField(_('Type name'), max_length=20, primary_key=True, unique=True)
    description = models.TextField(_('Type description'), max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return "Type: {}".format(self.name)
    
class Pokemon(models.Model):
    name = models.CharField(_("Pokemon name"), max_length=50)
    
    description = models.TextField(_("Pokemon description"), max_length=255, blank=True, null=True)
    
    type = models.ManyToManyField(
        to=PokeType,
        verbose_name=_("Pokemon type"),
        related_name='poke_type',
    )
    
    picture = models.ImageField(
        _("Pokemon picture"), 
        upload_to=poke_directory_path,
        blank=True, 
        null=True
    )
    
    height = models.PositiveIntegerField(_("Pokemon height"),
                                         help_text=_("Height of the pokemon in centimeters")
                                        )
    
    weight = models.PositiveIntegerField(_("Pokemon weight"),
                                         help_text=_("Pokemon weight in grams")
                                        )
    
    def __str__(self):
        return "Pokemon: {}".format(self.name)
