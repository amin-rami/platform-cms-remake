from django.contrib import admin
from cms.models import ProtectionLevel, TrendQuery



@admin.register(ProtectionLevel)
class ProtectionLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]


@admin.register(TrendQuery)
class TrendQueryAdmin(admin.ModelAdmin):
    list_display = ['id', 'protection_level', 'query', 'end_date', 'start_date']



