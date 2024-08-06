from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Vote
from .forms import PostForm, CommentForm
from .utils import embed_links
from django.utils.timezone import now


def post_list(request, **kwargs):
    hashtag = kwargs.get('hashtag')

    if not hashtag:
        posts = Post.objects.all()
        return render(request, 'blog/post-list.html', {'posts': posts})

    posts = Post.objects.filter(hashtags__name=hashtag)
    return render(request, 'blog/post-list.html', {'posts': posts,
                                                                        'hashtag': hashtag})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()
    formatted_content = embed_links(post.content)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=slug)

    return render(request, 'blog/post-detail.html', {'post': post,
                                                         'comments': comments,
                                                         'comment_form': comment_form,
                                                         'formatted_content': formatted_content})
@login_required
def like(request, slug):
    return __vote(request, slug, True)

@login_required
def dislike(request, slug):
    return __vote(request, slug, False)

def __vote(request, slug, is_liked):
    post = get_object_or_404(Post, slug=slug)

    # Users can't vote for their own posts
    if request.user == post.author:
        return redirect('post_detail', slug=slug)

    vote, created = Vote.objects.get_or_create(
        post=post,
        author=request.user
    )
    
    if not created:
        vote.date_created = now()

    vote.is_liked = is_liked
    vote.save()

    return redirect('post_detail', slug=slug)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post-create.html', {'form': form})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Ensure the logged-in user is the author of the post
    if request.user == post.author:
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('post_list')
    else:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('post_detail', slug=post.slug)