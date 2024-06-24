from django.contrib import admin
from .models import Inflow


class InflowAdmin(admin.ModelAdmin):
    search_fields = ('supplier__name', 'product__title', 'quantity',)
    list_display = ('supplier','product','quantity', 'created_at', 'updated_at',)
    
admin.site.register(Inflow, InflowAdmin)
