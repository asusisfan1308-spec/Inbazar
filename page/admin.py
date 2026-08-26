from django.contrib import admin
from .models import BranchLocation  # Импортируем правильную модель

@admin.register(BranchLocation)
class BranchLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'landmark')
    search_fields = ('name', 'address')
    list_filter = ('name',)