from django import forms
from .models import User, Event, League, Team

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class UserEditForm(forms.ModelForm):
    leagues = forms.ModelChoiceField(queryset=League.objects.all())
    #favorite_teams = forms.ModelMultipleChoiceField(queryset=Team.objects.all())


    class Meta:
        model = User
        fields = ['email', 'user_location', 'leagues', 'favorite_teams']
        widgets = {'favorite_teams': forms.SelectMultiple() }

class FavoriteTeamForm(forms.Form):
    leagues = forms.ModelChoiceField(queryset=League.objects.all())
    favorite_teams = forms.ModelMultipleChoiceField(queryset=Team.objects.all())

    class Meta:
        model = User
        fields = ['email', 'user_location', 'leagues', 'favorite_teams']

class TeamEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['favorite_teams']

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['fan_team', 'opp_team', 'event_date', 'event_time', 'bar', 'owner']
        widgets = {
            'event_date': DateInput(),
            'event_time': TimeInput()
        }

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_date', 'event_time', 'fan_team', 'opp_team']
        widgets = {
            'event_date': DateInput(),
            'event_time': TimeInput()
        }
