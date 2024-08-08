from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, UserDetailForm

# Create your views here.

@login_required
def user_profile_edit(request):
    """
    Displays the profile of a logged in user.

    **Context**

    ``post``
        An instance of :model:`userprofile.Profile`.

    **Template:**

    :template:`userprofile/userprofile_edit.html`
    """

    # Try to get the user's profile, or create one if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES,
        instance=profile)
        if profile_form.is_valid():
            profile.save()
    else:
        profile_form = ProfileForm(instance=profile)
    
    return render(
        request,
        "userprofile/userprofile_edit.html",
    {
        "profile_form": profile_form
    },
    )
