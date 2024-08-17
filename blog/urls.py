from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startup_page, name='start'),
    path('home/', views.PostList.as_view(), name='home'),
    path('about/', include('about.urls'), name='about'),
    path('create/', views.create_post, name='create_post'),
    path('search-result/', views.search_result, name='search_result'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/delete', views.delete_post, name='delete_post'),
    path('post/<slug:slug>/edit', views.edit_post, name='edit_post'),
    path('post/<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]