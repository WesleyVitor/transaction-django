from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.forms import CustomUserChangeForm, CustomUserCreationForm
from core.models import CustomUser, Ordinary, Shopkeeper, Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance','ordinary','shopkeeper',)
@admin.register(Ordinary)
class OrdinaryProfile(admin.ModelAdmin):
    list_display = ('full_name', 'user','cpf', 'wallet')
@admin.register(Shopkeeper)
class ShopKeeperProfile(admin.ModelAdmin):
    list_display = ('full_name', 'user','cpf', 'wallet')

class CustomUserAdmin(UserAdmin):
    add_form: Any = CustomUserCreationForm
    form = CustomUserChangeForm
    model= CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','cpf','full_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)