from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Team(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    team_name = models.CharField(max_length = 200, default = 'None')
    player1 = models.CharField(max_length=200, default = 'None')
    player2 = models.CharField(max_length=200, default = 'None')
    player3 = models.CharField(max_length=200, default = 'None')
    points = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default = timezone.now)

