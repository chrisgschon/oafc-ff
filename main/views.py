from django.shortcuts import render
from django.utils import timezone
from .models import Team, Player
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import TeamForm

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'players/player_list.html', {'players': players})

def player_details(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_details.html')

def manage(request):
    form = TeamForm
    return render(request, 'blog/post_edit.html', {'form': form})