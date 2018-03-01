from django import forms
from .models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'user_location']
