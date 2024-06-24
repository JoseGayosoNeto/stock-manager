from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title', 'brand__name', 'category__name',)
    list_display = ('title', 'brand', 'category', 'serie_number', 'cost_price', 'selling_price', 'quantity', 'created_at', 'updated_at',)

admin.site.register(Product, ProductAdmin)
