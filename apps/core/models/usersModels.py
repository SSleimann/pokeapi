from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from apps.core.utils import user_directory_path

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        _("email address"), 
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists.')
        }
    )
    
    is_verified = models.BooleanField(
        _('verified'),
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        verbose_name=_("user_profile"), 
        on_delete=models.CASCADE
    )
    
    picture = models.ImageField(
        _("user_picture"), 
        upload_to=user_directory_path,
        blank=True, 
        null=True
    )
    
    def __str__(self):
        """Return user's str representation."""
        return str(self.user)

