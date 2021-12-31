from worldcup22.models import Ticket,Match,Team
from .serializers import TicketSerializer,UserSerializer,MatchSerializer,TeamSerializer,UserCreateSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly

from rest_framework import generics, response,decorators, permissions,status, mixins,viewsets
#Register API
# class RegisterApi(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#     def post(self, request, *args,  **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user,    context=self.get_serializer_context()).data,
#             "message": "User Created Successfully.  Now perform Login to get your token",
#         })


from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)

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