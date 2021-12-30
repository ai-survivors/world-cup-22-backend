from rest_framework import serializers
from worldcup22.models import Ticket,Match,Team
from django.contrib.auth import get_user_model 

from rest_framework.permissions import IsAuthenticated
from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user


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

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        # fields = ('id','title','description','created_date', 'updated_date', 'price')



class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id','username')
        # fields = ('email','first_name','last_name','username','password')


