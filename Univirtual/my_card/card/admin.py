from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    fieldsets = [('Datos de la persona', {'fields': ['name', 'excel_file']})]
    list_display = ('name', 'excel_file')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Card, CardAdmin)
# Register your models here.
