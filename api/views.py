from rest_framework import generics
from worldcup22.models import Ticket
from .serializers import TicketSerializer

class TicketAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer