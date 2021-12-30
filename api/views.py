from worldcup22.models import Ticket,Match,Team
from .serializers import TicketSerializer,UserSerializer,MatchSerializer,TeamSerializer,RegisterSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets 




from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
#Register API
class RegisterApiViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
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
    serializer_class = MatchSerializer

class TeamViewSet(viewsets.ModelViewSet): # new
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer