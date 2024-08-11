from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm

# Create your views here.

@login_required
def user_profile(request, username):
    """
    Displays the profile of a logged in user.

    **Context**

    ``post``
        An instance of :model:`userprofile.Profile`.

    **Template:**

    :template:`userprofile/userprofile.html`
    """
    user = get_object_or_404(User, username=username)

    return render(
        request,
        "userprofile/userprofile.html",
    {
        "user": user
    },
    )
    

@login_required
def user_profile_edit(request):
    """
    Displays the edit page for a profile of a logged in user.

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
            profile = profile_form.save(commit=False)
        profile.save()
        messages.add_message(
                    request, messages.SUCCESS,
                    'Your profile has been updated.')
        return redirect("profile", username=request.user.username)

    else:
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        "userprofile/userprofile_edit.html",
    {
        "profile_form": profile_form
    },
    )

@login_required
def account_delete(request):
    """
    A view that allows the user to delete their profile permanently.
    """
    user = request.user

    if request.method == "POST":
        if user == request.user:
            user.delete()
            messages.success(
                request, "Your account has been deleted successfully."
            )
            return redirect("home")
        elif user != request.user:
                messages.add_message(
                    request, messages.ERROR,
                    'You cannot delete other peoples profiles!'
                )
                return redirect(reverse("home"))
    return render(request, "userprofile/delete_profile.html")

        
        
