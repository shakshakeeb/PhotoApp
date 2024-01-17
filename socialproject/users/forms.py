from django import forms
from django.contrib.auth.models import User
from .models import Profile

# form for editing user information
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        # specify the fields to include in the form
        fields = ('first_name', 'last_name', 'email')

# form for editing profile information
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        # specify the fields to include in the form
        fields = ('photo',)

# form for user login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# form for user registration
class UserRegistrationForm(forms.ModelForm):
    # additional password and confirmation fields
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        # specify the fields to include in the form
        fields = {'username', 'email', 'first_name'}

    def check_password(self):
        # custom validation to check if passwords match
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords dont match')
        return self.cleaned_data['password2']
