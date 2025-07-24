from django.urls import path
from .views import health, EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('health/', health, name='Health'),
    # Event CRUD endpoints
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-detail'),
]
