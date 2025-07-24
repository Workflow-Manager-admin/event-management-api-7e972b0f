from rest_framework import serializers
from .models import Event

# PUBLIC_INTERFACE
class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model."""

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'location',
            'start_time',
            'end_time',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
