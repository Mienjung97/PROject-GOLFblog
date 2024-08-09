from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from cloudinary.forms import CloudinaryFileField
from .models import Profile

class Handicap(forms.CharField):
    def clean(self, value):
        value = super().clean(value)
        float_value = float(value)
        if -4.4 <= float_value and float_value <= 54.0:
            return str(float_value)
        elif value.lower() in ("pro", "profi", "professional"):
            return str("Pro")
        else:
            return ValueError

class ProfileForm(forms.ModelForm):
    """
    A form for editing the info displayed on the users
    profile page.
    """
    first_name = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"placeholder": "First Name"}
        )
    )
    last_name = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"placeholder": "Last Name"}
        )
    )
    profile_picture = CloudinaryFileField(
        options= {
            'crop': 'limit', 'width': 333, 'height': 333,
        },
        required=False
    )
    handicap = Handicap(
        required=False, widget=forms.TextInput(
            attrs={"placeholder": 'Enter your handicap or "Pro"'}
        )
    )
    golfcourse = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={"placeholder": "Your home golf course"}
        )
    )
    user_bio = forms.CharField(
        required=False, widget=forms.Textarea(
            attrs={"placeholder": "Tell other users about yourself!"}
        )
    )

    class Meta:
        model = Profile
        fields = ("profile_picture", "first_name", "last_name", "handicap", "golfcourse", "user_bio")# 

class UserDetailForm(forms.ModelForm):
    """
    A form for the user to edit username and email.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))

    class Meta:
        model = User
        fields = ("username", "email")