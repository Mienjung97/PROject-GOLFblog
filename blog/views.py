from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post, Comment
from .forms import CommentForm, PostForm


# Create your views here.

def startup_page(request):
    """
    This decides on what page the the user starts the webpage:
    If the user is logged in from a previous session,
    they start on the blog page. If the user is logged out,
    they will start on the "about" page.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('about')

class PostList(generic.ListView):
    """
    generates a geneal list of all posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-pinned', '-created_on')
    template_name = "blog/index.html"
    paginate_by = 10
    context_object_name = 'post_list'

    # Rewrite this code - just for ideas!
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context['post_list']
        
        posts = posts.annotate(
            likes_count=Count('likes'),
            comments_count=Count('comments')
        )
        
        context['post_list'] = posts
        return context


@staff_member_required
def pin_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.pinned = not post.pinned # help from perplexity
    post.save()
    action = "pinned" if post.pinned else "unpinned" # help from perplexity

    return redirect('post_detail', slug=slug)

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    likes_count = post.likes.count()
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been submitted.'
            )
            return redirect('post_detail', slug=slug)

    return render(
        request,
        "blog/post_detail.html",
    {
        "post": post,
        "comments" : comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "likes_count": likes_count,
        "liked": liked,
    },
    )

# Code for creating, editing and deleting posts

@login_required
def create_post(request):
    """
    Display an individual post to create.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/create_post.html`
    """

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        print("Files:", request.FILES) 
        if post_form.is_valid():
            print("Form is valid. Data:", post_form.cleaned_data)
            post = post_form.save(commit=False)
            post.author = request.user
            print("Assigned author:", post.author)
            if not post.slug:
                post.slug = slugify(post.title)
                print("Generated slug:", post.slug)
            if 'featured_image' in post_form.cleaned_data and post_form.cleaned_data['featured_image']:
                post.featured_image = post.featured_image = post_form.cleaned_data['featured_image']
            else:
                post.featured_image = None
            post.save()
            print('POST: ', post)
            print("post has been saved")
            messages.add_message(
                request, messages.SUCCESS,
                'Your post has been submitted.')
            return redirect("home")
            

        else:
            print("Form errors:", post_form.errors)

    else:
        post_form = PostForm()
    
    return render(
        request,
        "blog/create_post.html",
    {
        "post_form": post_form,
    },
    )

@login_required
def delete_post(request, slug):
    """
    A view that allows the user to delete a post permanently.
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        if request.user == post.author:
            post.delete()
            messages.success(
                request, "Your account has been deleted successfully."
            )
            return redirect("home")
        else:
            messages.add_message(
                request, messages.ERROR,
                'You cannot delete other peoples posts!'
            )
            return redirect(reverse("home"))

    return render(
        request, 
        "blog/delete_post.html",
        {
            'post':post
        })

@login_required
def edit_post(request, slug):
    """
    Display an individual post to edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``post_form``
        An instance of :form:`blog.PostForm`.

    **Template:**

    :template:`blog/edit_post.html`
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            if not post.slug:
                post.slug = slugify(post.title)
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your post has been updated.'
            )
            if post.status == 1:
                return redirect('post_detail', slug=post.slug)
            else:
                return redirect('posts_drafts')
    else:
        post_form = PostForm(instance=post)
    
    return render(
        request,
        "blog/edit_post.html",
        {
            'post_form': post_form,
            'post': post
        }
    )

# Likes (code was influenced by YouTube channel "Codemy.com")

def like_post(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_slug')) #grabs like button via name
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Comment section

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context:**

    ``post``
        An instance of :model:`blog.Post`
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:blog.`CommentForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Search function

def search_result(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        post_results = Post.objects.filter(
            Q(title__icontains=searched) |
            Q(author__username__icontains=searched) |
            Q(content__icontains=searched) |
            Q(excerpt__icontains=searched),
            status=1
        )

        comment_results = Comment.objects.filter(
            Q(author__username__icontains=searched) |
            Q(body__icontains=searched)
        )

        user_results = User.objects.filter(
            Q(username__icontains=searched)
        )

    else:
        return redirect('home')

    return render(
        request,
        'blog/search_results.html',
        {
            'searched': searched,
            'post_results': post_results,
            'comment_results': comment_results,
            'user_results': user_results,
        }
    )
    
