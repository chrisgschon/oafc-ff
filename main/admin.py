from django.contrib import admin
from .models import Team
from .models import Player

admin.site.register(Player)
admin.site.register(Team)
