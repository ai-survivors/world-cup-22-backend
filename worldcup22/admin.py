from django.contrib import admin
from .models import Ticket,Team,Match



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = [
        "title",
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