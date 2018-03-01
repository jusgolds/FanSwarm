from django import forms
from .models import User, Event

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'user_location']

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_date', 'event_time', 'fan_team', 'opp_team']
