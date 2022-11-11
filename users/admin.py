from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users


class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ['email', 'name', 'password', 'surname', 'login']


admin.site.register(Users, CustomUserAdmin)
