from django.shortcuts import render, redirect
from community.forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
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
    return render(request, 'community/write.html', {'form':form})
@login_required(login_url='users:login')
def modify(request, num):
    article = get_object_or_404(Article, id=num)
    if request.user != article.name:
        messages.error(request, "수정 권한이 없습니다")
        return redirect('community:view',num=num)
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            article.title = request.POST['title']
            article.contents = request.POST['contents']
            article.mdate = timezone.now()
            article.save()
            return redirect('/posts')
    else:
        form = Form()
    return render(request, 'community/modify.html', {'form':form, 'article':article})
@login_required(login_url='users:login')
def delete(request, num):
    article = get_object_or_404(Article,id=num)
    if request.user != article.name:
        messages.error(request, "삭제 권한이 없습니다")
        return redirect('community:view',num=num)
    else:
        article.delete()
        return redirect('community:posts')
def posts(request):
    articleList = Article.objects.all()
    return render(request, 'community/posts.html', {'articleList':articleList})
def view(request, num):
    article = Article.objects.get(id=num)
    return render(request, 'community/view.html', {'article':article})
def comment_create(request, num):
    article = get_object_or_404(Article,id=num)
    comment = Comment(article=article, contents = request.POST.get('content'), cdate = timezone.now())
    comment.save()
    return redirect('community:view', num=num)