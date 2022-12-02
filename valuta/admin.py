from django.contrib import admin
from .models import Valuta, Value

admin.site.register(Valuta)


@admin.register(Value)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('volume', 'price', 'market_capital', 'changes_24hour')
