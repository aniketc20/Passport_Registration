from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import RegistrationForm, CustomUserChangeForm


class AccountAdmin(UserAdmin):
    add_form = RegistrationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ('email', 'image', 'is_staff', 'is_active', 'd_o_b', 'passport_number', 'phone_number', 'full_name')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'image', 'd_o_b', 'passport_number', 'phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'd_o_b', 'full_name', 'image', 'passport_number', 'phone_number', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Account, AccountAdmin)
