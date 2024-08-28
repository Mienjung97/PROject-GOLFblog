from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Creates an admin panel for heroku to create, modify and delete
    comments on posts.
    """

    list_display = ('title', 'slug', 'status', 'created_on', 'pinned')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'pinned')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['pin_posts', 'unpin_posts']

    def pin_posts(self, request, queryset):
        queryset.update(pinned=True)

    def unpin_posts(self, request, queryset):
        queryset.update(pinned=False)


# Register your models here.
admin.site.register(Comment)
