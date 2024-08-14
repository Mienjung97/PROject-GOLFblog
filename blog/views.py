from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
def startup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('about')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 20

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

    return render(
        request,
        "blog/post_detail.html",
    {
        "post": post,
        "comments" : comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
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
            return redirect('post_detail', slug=post.slug)
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