from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ArtistProfile, ClientProfile

class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Register as"
    )
    email = forms.EmailField(
        required=True,
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'role')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Choose a username',
                'class': 'form-control'
            }),
        }
        labels = {
            'username': 'Username'
        }

class ArtistProfileForm(forms.ModelForm):
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your artistic bio here...',
            'rows': 4,
            'class': 'form-control'
        }),
        label="Artist Bio"
    )
    profile_pic = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label="Profile Picture"
    )

    class Meta:
        model = ArtistProfile
        fields = ('bio', 'profile_pic')

class ClientProfileForm(forms.ModelForm):
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your address',
            'class': 'form-control'
        }),
        label="Address"
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone number (e.g., +1 555-555-5555)',
            'class': 'form-control'
        }),
        label="Phone Number"
    )

    class Meta:
        model = ClientProfile
        fields = ('address', 'phone')