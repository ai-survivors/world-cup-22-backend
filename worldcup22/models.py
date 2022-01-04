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
    number_of_tickets_A=models.IntegerField(default=2000)
    number_of_tickets_B=models.IntegerField(default=3000)
    number_of_tickets_C=models.IntegerField(default=15000)
    number_of_tickets_D=models.IntegerField(default=20000)


    team1 = models.ForeignKey(
        Team,related_name='team1', on_delete=models.CASCADE, null=True, blank=True
    )
    team2 = models.ForeignKey(
        Team,related_name='team2', on_delete=models.CASCADE, null=True, blank=True
    )
    votes_team1 = models.IntegerField(default=0)
    votes_team2 = models.IntegerField(default=0)

    time =models.CharField(max_length=64)
    match_date=models.CharField(max_length=64)
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
    ticket_class=models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
  
    
    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)

        self.match.number_of_tickets = F('number_of_tickets')-1
        if self.ticket_class=="A":
            self.match.number_of_tickets_A = F('number_of_tickets_A')-1
        if self.ticket_class=="B":
            self.match.number_of_tickets_B = F('number_of_tickets_B')-1
        if self.ticket_class=="C":
            self.match.number_of_tickets_C = F('number_of_tickets_C')-1
        if self.ticket_class=="D":
            self.match.number_of_tickets_D = F('number_of_tickets_D')-1
        self.match.save()

    def __str__(self):
        return self.match.title

class Vote(models.Model):
    owner = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, null=True, blank=True )
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, null=True, blank=True
    )
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True
    )
    voted = models.BooleanField(default = True)

    
    def save(self, *args, **kwargs):
        super(Vote  , self).save(*args, **kwargs)

        if self.team.country==self.match.team1.country:
          self.match.votes_team1 = F('votes_team1')+1 
       
        else:

              self.match.votes_team2 = F('votes_team2')+1
     
        self.match.save()

    def __str__(self):
        return self.team.country

class New(models.Model):
    title = models.CharField(max_length=128)
    img=   models.TextField(default="",)
    link=  models.TextField(default="",)
    date= models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=64)
    email=  models.CharField(max_length=128)
    message=  models.TextField(default="",)
   

    def __str__(self):
        return self.name
