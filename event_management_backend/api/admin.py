from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin interface for managing events."""
    list_display = ('id', 'title', 'start_time', 'end_time', 'location', 'created_at', 'updated_at')
    search_fields = ('title', 'location')
    ordering = ('-created_at',)
