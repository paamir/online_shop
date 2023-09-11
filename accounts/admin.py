from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser
from .forms import UserCreateCustomForm, UserChangeCustomForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreateCustomForm
    form = UserChangeCustomForm
    list_display = ['email', 'username']
