from django.contrib import admin
from .models import Users, UserProfile


admin.site.register(UserProfile)
admin.site.register(Users)
