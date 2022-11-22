from django.contrib import admin
from .models import Users, UserProfile


@admin.register(Users)
class MyAdmin(admin.ModelAdmin):
    list_display = ('email', 'username',  'is_active', 'phone')


@admin.register(UserProfile)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')

# admin.site.register(UserProfile)
# admin.site.register(Users)
