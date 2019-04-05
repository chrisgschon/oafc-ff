from django import forms

from .models import Team, Player

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('Pick 1', 'Pick 2', 'Pick 3')
        players = forms.ModelMultipleChoiceField(queryset=Player.objects.all())
        