from django.shortcuts import render, redirect
from community.forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='users:login')
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
            return redirect('/posts')
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})
@login_required(login_url='users:login')
def modify(request, num):
    article = get_object_or_404(Article, id=num)
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            article.title = request.POST['title']
            article.contents = request.POST['contents']
            article.save()
            return redirect('/posts')
    else:
        form = Form()
    return render(request, 'modify.html', {'form':form, 'article':article})
@login_required(login_url='users:login')
def delete(request, num):
    article = get_object_or_404(Article,id=num)
    article.delete()
    return redirect('/posts')
def posts(request):
    articleList = Article.objects.all()
    return render(request, 'posts.html', {'articleList':articleList})
def view(request, num):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})