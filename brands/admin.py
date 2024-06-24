from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'created_at', 'updated_at',)
    
admin.site.register(Brand, BrandAdmin)
