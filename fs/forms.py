from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Event, League, Team


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]


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
