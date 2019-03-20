from django.shortcuts import render
from django.utils import timezone
from .models import Team
from django.shortcuts import render, get_object_or_404, redirect


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})