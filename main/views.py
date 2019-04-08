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
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.manager = request.user
            team.save()
            team.players.set(form.cleaned_data['players'])
            
    else:
        form = TeamForm
    return render(request, 'manage/manage_team.html', {'form': form})

# def some_view(request):
#     if request.method == 'POST':
#         form = SomeForm(request.POST)
#         if form.is_valid():
#             picked = form.cleaned_data.get('picked')
#             # do something with your results
#     else:
#         form = SomeForm

#     return render_to_response('some_template.html', {'form':form },
#         context_instance=RequestContext(request))    