from rest_framework import generics , permissions
from worldcup22.models import Ticket,Match
from .serializers import TicketSerializer,UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets 

# class TicketAPIView(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAdminUser,) 
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
    
# class TicketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAdminUser,) 
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer


class TicketViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class MatchViewSet(viewsets.ModelViewSet): # new
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Match.objects.all()
    serializer_class = TicketSerializer


class UserViewSet(viewsets.ModelViewSet): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer