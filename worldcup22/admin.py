from django.contrib import admin
from .models import Ticket



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

 