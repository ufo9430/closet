from django.shortcuts import render, redirect
from community.forms import *
# Create your views here.

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts')
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})
def modify(request, num):
    article = Article.objects.get(id=num)
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            article.title = request.POST['title']
            article.contents = request.POST['contents']
            article.save()
            return redirect('/posts')
    else:
        form = Form()
    return render(request, 'modify.html', {'form':form})
def posts(request):
    articleList = Article.objects.all()
    return render(request, 'posts.html', {'articleList':articleList})
def view(request, num):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})
def delete(request, num):
    article = Article.objects.get(id=num)
    article.delete()
    return redirect('/posts')