from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from aircraft_production.models import Team, Aircraft


class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=True, label="Team")

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2', 'team']

class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ProducePartForm(forms.Form):
        aircraft = forms.ModelChoiceField(queryset=Aircraft.objects.all(), label="Uçak Seçin")
        quantity = forms.IntegerField(min_value=1, label="Adet")