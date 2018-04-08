from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Event, League, Team


class CustomSelectMultiple(forms.SelectMultiple):
    def __init__(self, attrs=None, choices=()):
        self.custom_attrs = {}
        super().__init__(attrs, choices)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        index = str(index) if subindex is None else "%s_%s" % (index, subindex)
        if attrs is None:
            attrs = {}
        option_attrs = self.build_attrs(self.attrs, attrs) if self.option_inherits_attrs else {}
        if selected:
            option_attrs.update(self.checked_attribute)
        if 'id' in option_attrs:
            option_attrs['id'] = self.id_for_label(option_attrs['id'], index)

        # setting the attributes here for the option
        if len(self.custom_attrs) > 0:
            if value in self.custom_attrs:
                custom_attr = self.custom_attrs[value]
                for k, v in custom_attr.items():
                    option_attrs.update({k: v})

        return {
            'name': name,
            'value': value,
            'label': label,
            'selected': selected,
            'index': index,
            'attrs': option_attrs,
            'type': self.input_type,
            'template_name': self.option_template_name,
        }

class TeamMultipleChoiceField(forms.ModelMultipleChoiceField):

    # custom method to label the option field
    def label_from_instance(self, obj):
        # since the object is accessible here you can set the extra attributes
        self.widget.custom_attrs.update({obj.pk: {'data-league': obj.team_league.abbreviation}})
        return obj.team_name


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
    leagues = forms.ModelChoiceField(queryset=League.objects.all(), empty_label=None)
    favorite_teams = TeamMultipleChoiceField(queryset=Team.objects.all(), widget=CustomSelectMultiple())

    class Meta:
        model = User
        fields = ['name', 'email', 'user_location', 'leagues', 'favorite_teams']
        #widgets = {'favorite_teams': forms.SelectMultiple() }


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
