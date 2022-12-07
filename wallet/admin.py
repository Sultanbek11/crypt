from django.contrib import admin
from .models import Wallet, WalletValutes


# Register your models here.
@admin.register(Wallet)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('owners', 'summ_in_dollar')

admin.site.register(WalletValutes)
