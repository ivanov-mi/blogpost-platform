from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post-list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})