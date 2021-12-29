from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "mobile"
        
    ]

    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] =  ("Personal info", {'fields':('first_name', 'last_name', 'email',"mobile")})
    UserAdmin.fieldsets = tuple(fieldsets)


admin.site.register(CustomUser, CustomUserAdmin)
