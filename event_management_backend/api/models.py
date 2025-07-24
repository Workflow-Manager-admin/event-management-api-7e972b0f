from django.db import models

# PUBLIC_INTERFACE
class Event(models.Model):
    """
    Model representing an event in the system.

    Fields:
        - title (str): Title of the event.
        - description (str): A brief description of the event.
        - location (str): Location where the event is held.
        - start_time (datetime): Start time of the event.
        - end_time (datetime): End time of the event.
        - created_at (datetime): DateTime the event was created (read-only).
        - updated_at (datetime): DateTime the event was last updated (read-only).
    """

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time the event was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Time the event was last updated")

    def __str__(self):
        return self.title
