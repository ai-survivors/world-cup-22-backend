from worldcup22.models import Ticket,Match,Team,Vote,New,Feedback
from .serializers import TicketSerializer,UserSerializer,MatchSerializer,TeamSerializer,UserCreateSerializer,VoteSerializer,NewsSerializer,FeedbackSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import generics, response,decorators, permissions,status, mixins,viewsets
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,) 
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get(request, pk, format=None, *args, **kwargs):
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



class TicketViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


def buyticket(request):
    username=request.user.username

    message=f'Hello {username} thanks for your request We have checked your Vaccination Certificate and It was Correct Here is Your ticket Link'

    send_mail(
       'Qatar 2022 Buying ticket',
        message,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False,
    )
    return HttpResponseRedirect("http://localhost:3000/Profile")


class MatchViewSet(viewsets.ModelViewSet): # new
    permission_classes = (permissions.AllowAny,) 

    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class VoteViewSet(viewsets.ModelViewSet): # new
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class TeamViewSet(viewsets.ModelViewSet): # new
    permission_classes = (permissions.AllowAny,) 

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class NewsViewSet(viewsets.ModelViewSet): # new
    permission_classes = (permissions.AllowAny,)
    queryset = New.objects.all()
    serializer_class = NewsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





class UserViewSet(viewsets.ModelViewSet): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class FeedbackViewSet(viewsets.ModelViewSet): 
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


    