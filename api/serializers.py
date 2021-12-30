from rest_framework import serializers
from worldcup22.models import Ticket,Match
from django.contrib.auth import get_user_model 

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        # fields = ('id','title','description','created_date', 'updated_date', 'price')

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        # fields = ('id','title','description','created_date', 'updated_date', 'price')



class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id','username')
        # fields = ('email','first_name','last_name','username','password')


