from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.models import User, Profile

class UserAdminView(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "username")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_verified",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "is_verified")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = ["date_joined"]
    
    actions = ['make_verified']

    @admin.action(description='Make selected users verified')
    def make_verified(self, request, queryset):
        queryset.update(is_verified=True)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)

admin.site.register(User, UserAdminView)
admin.site.register(Profile, ProfileAdmin)