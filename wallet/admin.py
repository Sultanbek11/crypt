from django.contrib import admin
from .models import Wallets


# Register your models here.
@admin.register(Wallets)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('owners', 'summ_in_dollar', 'title_valute')
