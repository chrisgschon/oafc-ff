from django.shortcuts import render
from django.utils import timezone
from .models import Player
from django.shortcuts import render, get_object_or_404, redirect


def player_list(request):
    players = Player.objects.all()
    return render(request, 'players/player_list.html', {'players': players})

def player_details(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_details.html')
