# from django.urls import path
# from .views import TicketAPIView , TicketDetailAPIView


# urlpatterns = [
# path('tickets/', TicketAPIView.as_view()),
# path('tickets/<int:pk>', TicketDetailAPIView.as_view()),
# ]
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, TicketViewSet,MatchViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('tickets', TicketViewSet, basename='tickets')
router.register('matches', MatchViewSet, basename='matches')

urlpatterns = router.urls