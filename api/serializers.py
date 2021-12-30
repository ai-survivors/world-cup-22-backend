from rest_framework import serializers
from worldcup22.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        # fields = ('id','title','description','created_date', 'updated_date', 'price')