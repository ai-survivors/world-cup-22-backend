from django.urls import path
from .views import TicketAPIView


urlpatterns = [
path('', TicketAPIView.as_view()),
]
