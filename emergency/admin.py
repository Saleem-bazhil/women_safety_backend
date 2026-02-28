from django.contrib import admin
from .models import EmergencyContact, SOSAlert

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'user', 'is_primary')
    search_fields = ('name', 'phone', 'user__username')

@admin.register(SOSAlert)
class SOSAlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'status', 'latitude', 'longitude')
    list_filter = ('status', 'timestamp')
    search_fields = ('user__username',)
