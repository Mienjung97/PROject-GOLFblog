from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from cloudinary.forms import CloudinaryFileField
from .models import Profile

class Handicap(forms.CharField):
    def clean(self, value):
        value = super().clean(value)

        if value == "":
            return value

        try:
            float_value = float(value)
            if -4.4 <= float_value and float_value <= 54.0:
                return str(float_value)
        except ValueError:
            if value.lower() in ("pro", "profi", "professional"):
                return str("Pro")
        raise forms.ValidationError("Invalid handicap value")


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
        fields = ("profile_picture", "first_name", "last_name", "handicap", "golfcourse", "user_bio")
