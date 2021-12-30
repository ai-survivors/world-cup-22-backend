from rest_framework import generics , permissions
from worldcup22.models import Ticket
from .serializers import TicketSerializer

class TicketAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,) 
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
class TicketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,) 
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer