from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=200, default = 'None')
    position = models.CharField(max_length=200, default = 'None')
    goals = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    owngoals = models.PositiveIntegerField()
    cleansheets = models.PositiveIntegerField()
    yellowcards = models.PositiveIntegerField()
    redcards = models.PositiveIntegerField()
    motms = models.PositiveIntegerField()
    points = models.PositiveIntegerField()

    # bio = models.CharField(max_length=1000, default = 'None')


    