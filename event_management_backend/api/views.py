from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

@api_view(['GET'])
def health(request):
    """Health check endpoint."""
    return Response({"message": "Server is up!"})

# PUBLIC_INTERFACE
class EventListCreateAPIView(generics.ListCreateAPIView):
    """
    get:
    List all events.

    post:
    Create a new event.
    """
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer

# PUBLIC_INTERFACE
class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve an event by ID.

    put:
    Update an event by ID.

    patch:
    Partially update an event by ID.

    delete:
    Delete an event by ID.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
