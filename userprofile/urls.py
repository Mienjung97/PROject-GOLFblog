from django.urls import path
from . import views

urlpatterns = [
    path('userprofile/<str:username>/', views.user_profile, name='profile'),
    path('edit/', views.user_profile_edit, name='profile_edit'),
    path('edit/user', views.user_detail_edit, name='username_edit'),
]