from django.contrib import admin
from .models import Ticket,Team,Match,Vote,New,Feedback



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = [
        "match",
        "created_date",
        "updated_date",
        "price",
        "description",
        "owner",
        
    ]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    list_display = [
       'country'
        
    ]

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):

   
    list_display = [
        'title',
       'team1',
       'team2'
        
    ]
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):

   
    list_display = [
        'owner',
       'match',
       'team'
        
    ]
    

@admin.register(New)
class NewsAdmin(admin.ModelAdmin):

   
    list_display = [
        'title',
        'img',
        'link',
        'date'
        
    ]
    

    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

   
    list_display = [
        'name',
        'email',
        'message',
      
        
    ]
    