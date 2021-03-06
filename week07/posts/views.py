from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
import pdb

# Post
def new(request):
    return render(request, 'posts/new.html')

def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    return render(request, 'posts/create.html', {'form': form})

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/show.html', {"post": post})
    
def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/update.html', {"post": post})
    
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('home')
    
# Comment
def new_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/new_comment.html', {'post': post})
    
    
def create_comment(request, id):
    form = CommentForm()
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:show', post.id)
    return render(request, 'posts/new_comment.html', {'form': form})
    