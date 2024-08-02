from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post-list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)

    return render(request, 'blog/post-detail.html', {'post': post,
                                                         'comments': comments,
                                                         'comment_form': comment_form})

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.likes += 1
    post.save()
    return redirect('post_detail', slug=slug)

def dislike(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.dislikes += 1
    post.save()
    return redirect('post_detail', slug=slug)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
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