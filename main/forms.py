from django import forms

from .models import Team, Player

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name','players',)

    def __init__ (self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields["players"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["players"].queryset = Player.objects.all()


# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
        
#         # Check if a date is not in the past. 
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))

#         # Check if a date is in the allowed range (+4 weeks from today).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

#         # Remember to always return the cleaned data.
#         return data

# class IngredientForm (forms.ModelForm):
#     class Meta:
#         model = Ingredient
#         exclude = ["franchise"]

#     def __init__ (self, *args, **kwargs):
#         brand = kwargs.pop("brand")
#         super(IngredientForm, self).__init__(*args, **kwargs)
#         self.fields["diets"].widget = forms.widgets.CheckboxSelectMultiple()
#         self.fields["diets"].help_text = ""
#         self.fields["diets"].queryset = Diet.objects.all()
#         self.fields["preferences"].widget = forms.widgets.CheckboxSelectMultiple()
#         self.fields["preferences"].help_text = ""
#         self.fields["preferences"].queryset = FoodPreference.objects.filter(franchise=brand)
