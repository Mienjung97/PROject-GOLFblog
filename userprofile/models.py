from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    """
    Stores the information about the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
    related_name="profile")
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    profile_picture = CloudinaryField('profileimage', default='placeholder', 
    blank=True, null=True)
    handicap = models.CharField(max_length=12, null=True, blank=True)
    golfcourse = models.CharField(max_length=50, null=True, blank=True)
    user_bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s page"