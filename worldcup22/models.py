from django.contrib.auth import get_user_model
from django.db import models 
from django.db.models import F



class Team(models.Model):
    country = models.CharField(max_length=64)
    flag= models.TextField(default="",)

  

    def __str__(self):
        return self.country



class Match(models.Model):
   
    title = models.CharField(max_length=64)
    stadium = models.CharField(max_length=64,default="")
    number_of_tickets=models.IntegerField(default=40000)
    team1 = models.ForeignKey(
        Team,related_name='team1', on_delete=models.CASCADE, null=True, blank=True
    )
    team2 = models.ForeignKey(
        Team,related_name='team2', on_delete=models.CASCADE, null=True, blank=True
    )
    votes_team1 = models.IntegerField(default=0)
    votes_team2 = models.IntegerField(default=0)


    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
    description = models.TextField(default="", null=True, blank=True)
   

    def __str__(self):
        return self.title



class Ticket(models.Model):
    owner = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, null=True, blank=True )
    description = models.TextField(default="", null=True, blank=True)
    price= models.FloatField( default=None)
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, null=True, blank=True
    )

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    purchased = models.BooleanField(default = False)
    
    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)
        self.match.number_of_tickets = F('number_of_tickets')-1
        self.match.save()

    def __str__(self):
        return self.match.title
