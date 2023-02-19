from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.core.models import User, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_verified')
    list_filter = ('is_verified', 'is_staff')
    
    actions = ['make_verified']

    @admin.action(description='Make selected users verified')
    def make_verified(self, request, queryset):
        queryset.update(is_verified=True)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'picture')
    list_filter = ('user',)
