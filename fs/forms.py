from django import forms
from .models import User, Event, League, Team

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class UserEditForm(forms.ModelForm):
    leagues = forms.ModelChoiceField(queryset=League.objects.all())

    class Meta:
        model = User
        fields = ['email', 'user_location', 'leagues', 'favorite_teams']
        widgets = {'favorite_teams': forms.SelectMultiple() }


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['team_league', 'fan_team', 'opp_team', 'event_date', 'event_time', 'bar', 'owner']
        widgets = {
            'event_date': DateInput(),
            'event_time': TimeInput()
        }

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_date', 'event_time', 'team_league', 'fan_team', 'opp_team']
        widgets = {
            'event_date': DateInput(),
            'event_time': TimeInput()
        }
