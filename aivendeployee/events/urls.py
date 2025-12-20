from django.urls import path
from .views import create_event, get_events, update_event, delete_event

urlpatterns = [
    path("create-event/", create_event),
    path("events/", get_events),
    path("update-event/<int:id>/", update_event),
    path("delete-event/<int:id>/", delete_event),
]
