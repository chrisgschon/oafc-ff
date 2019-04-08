from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
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
    def __str__(self):
        return self.name


class Team(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    team_name = models.CharField(max_length = 200, default = 'None')
    players = models.ManyToManyField(Player)
    points = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.team_name


from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


def players_changed(sender, **kwargs):
    if kwargs['instance'].players.count() > 3 or kwargs['instance'].players.count() <3:
        raise ValidationError("Please pick 3 players")


m2m_changed.connect(players_changed, sender=Team.players.through)
        




