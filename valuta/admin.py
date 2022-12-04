from django.contrib import admin
from .models import Value

# admin.site.register(Valuta)


@admin.register(Value)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'volume', 'price', 'changes_12hour')