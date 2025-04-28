from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ArtistProfile, ClientProfile

class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'role')

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ('bio', 'profile_pic')

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ('address', 'phone')