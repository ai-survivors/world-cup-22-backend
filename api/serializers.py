from rest_framework import serializers
from worldcup22.models import Ticket,Match,Team,Vote,New
from django.contrib.auth import get_user_model 

from rest_framework.permissions import IsAuthenticated
from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type":   "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
            
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if (email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(TicketSerializer, self).to_representation(instance)
        rep['match'] = instance.match.title
        return rep




class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    def to_representation(self, instance):
        rep1 = super(MatchSerializer, self).to_representation(instance)
        rep1['team1'] = {"country":instance.team1.country,"flag":instance.team1.flag}
        rep1['team2'] = {"country":instance.team2.country,"flag":instance.team2.flag}
        

        return rep1

   

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'



class VoteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Vote
        fields ='__all__'
    def to_representation(self, instance):

        rep1 = super(VoteSerializer, self).to_representation(instance)
        rep1['owner'] = instance.owner.username
        rep1['match'] = {"matchid":instance.match.id,"title":instance.match.title,"team1":instance.match.team1.country,"team2":instance.match.team2.country}
        rep1['team'] = instance.team.country
        

        

        return rep1

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id','username')
        # fields = ('email','first_name','last_name','username','password')


