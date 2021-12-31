# from django.urls import path
# from .views import TicketAPIView , TicketDetailAPIView


# urlpatterns = [
# path('tickets/', TicketAPIView.as_view()),
# path('tickets/<int:pk>', TicketDetailAPIView.as_view()),
# ]
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, TicketViewSet,MatchViewSet,TeamViewSet,RegistrationViewSet,VoteViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

# router.register('register', RegisterApiViewSet, basename='register')


# urlpatterns = [
#  path('register/', registration, name='register')
# ]

# path('register/', RegisterApi.as_view()),
router.register('tickets', TicketViewSet, basename='tickets')
router.register('matches', MatchViewSet, basename='matches')
router.register('teams', TeamViewSet, basename='teams')
router.register('register', RegistrationViewSet, basename='register')
router.register('votes', VoteViewSet, basename='votes')




urlpatterns = router.urls