from django.contrib import admin
from .models import Wallet, WalletValutes, Purchase, PurchaseInfo, Sell


# Register your models here.
@admin.register(Wallet)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('owner', 'summ_in_dollar', 'wallets_token')


@admin.register(WalletValutes)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title_valute')


@admin.register(Purchase)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'valuta', 'amount')


@admin.register(PurchaseInfo)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created')

@admin.register(Sell)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'valuta', 'amount')

# admin.site.register(WalletValutes)
# admin.site.register(OrderInfo)
# admin.site.register(Order)
