from django.urls import path
from . import views

urlpatterns = [
    path('userprofile/posts/', views.view_user_postlist, name='profile_posts'),
    path('userprofile/<str:username>/', views.user_profile, name='profile'),
    path('edit/', views.user_profile_edit, name='profile_edit'),
    path('account_delete/', views.account_delete, name='account_delete'),
]

#