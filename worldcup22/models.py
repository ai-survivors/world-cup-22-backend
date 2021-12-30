from django.contrib.auth import get_user_model
from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=64)

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    price= models.FloatField( default=None)
    # category = models.c
   

    def __str__(self):
        return self.title
