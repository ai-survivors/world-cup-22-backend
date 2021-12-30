from django.urls import path
from .views import TicketAPIView , TicketDetailAPIView


urlpatterns = [
path('tickets/', TicketAPIView.as_view()),
path('tickets/<int:pk>', TicketDetailAPIView.as_view()),
]
