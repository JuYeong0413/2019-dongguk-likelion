from django.shortcuts import render, redirect, get_object_or_404 #없으면 404 에러를 띄워주겠다
from .models import Post

# Create your views here.
def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content) #.save 안해도 객체가 생성된다
        return redirect('list') #redirect 반드시 return 써야한다. 안그러면 동작안함


def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'all_posts': posts})


def show(request, id): #id 받는 것
    # post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id) #Post에서 찾는다, pk=id인거
    return render(request, 'posts/show.html', {'post': post})


def update(request, id):
    # post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title #post의 title에 title을 담아주겠다
        post.content = content
        post.save()
        return redirect('show', post.pk)
    return render(request, 'posts/update.html', {'post': post}) #views->urls->html작업


def delete(request, id):
    # post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.delete()
        return redirect('list')