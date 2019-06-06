from django.shortcuts import render, redirect
from posts.models import Post

# Create your views here.
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title=title, content=content)
        post.save()
        return redirect('list')
        
    return render(request, 'posts/create.html')


def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})