from django.contrib import admin
from .models import Account


# Register your models here.
@admin.register(Account)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('owners', 'summ_in_dollar', 'title_valute')
