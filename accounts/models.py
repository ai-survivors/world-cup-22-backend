from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
      mobile = models.CharField(default="",max_length=16)
    
    # add additional fields in here
      def __str__(self):
         return self.username

   