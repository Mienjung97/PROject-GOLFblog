from django import forms
from .models import Comment, Post
from cloudinary.forms import CloudinaryFileField


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

    featured_image = CloudinaryFileField(
        options={
            'crop': 'limit',
            'width': 600,
            'height': 600,
        },
        required=False,
    )

    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'content', 'status', 'excerpt')
