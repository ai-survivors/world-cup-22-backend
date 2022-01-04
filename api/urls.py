
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, TicketViewSet,MatchViewSet,TeamViewSet,RegistrationViewSet,VoteViewSet,NewsViewSet,buyticket,FeedbackViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

# router.register('register', RegisterApiViewSet, basename='register')


urlpatterns = [
 path('buyticket/', buyticket, name='buyticket')
]

# path('register/', RegisterApi.as_view()),
router.register('tickets', TicketViewSet, basename='tickets')
# router.register('buyticket', buyticket, basename='buyticket')

router.register('matches', MatchViewSet, basename='matches')
router.register('teams', TeamViewSet, basename='teams')
router.register('register', RegistrationViewSet, basename='register')
router.register('votes', VoteViewSet, basename='votes')
router.register('news', NewsViewSet, basename='news')
router.register('feedbacks', FeedbackViewSet, basename='feedbacks')




urlpatterns += router.urls