from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    # Extending the UserCreationForm to add an email field to the form
    # This is the form that will be used to register a new user
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
