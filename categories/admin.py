from django.contrib import admin
from.models import Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_at', 'updated_at',)
    

admin.site.register(Category, CategoryAdmin)
