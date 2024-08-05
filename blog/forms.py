from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    """
    Adds the form for commenting on a post.
    """
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    """
    Adds the form for creating a post.
    """
    class Meta:
        model = Post
        fields = ('title', 'author', 'featured_image', 'content', 'status')