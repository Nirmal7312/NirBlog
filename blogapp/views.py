from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blogs


def index(request):
    blog_all = Blogs.objects.all()
    return render(request, 'index.html', {'blogs': blog_all})


def adding(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        blog = request.POST.get('blog')
        image = request.FILES.get('image')
        print(title)
        blogs = Blogs(title=title, desc=blog, img=image)
        blogs.save()
    return redirect('index')


def add(request):
    return render(request, 'add.html')


def post(request, pid):
    post = get_object_or_404(Blogs, id=pid)
    print(post)
    return render(request, 'post.html', {'post': post})


def delete(request, did):
    dpost = get_object_or_404(Blogs, id=did)
    print(dpost)
    dpost.delete()
    return redirect('index')


def edit(request, did):
    post = get_object_or_404(Blogs, id=did)
    return render(request, 'edit.html', {'post':post})


def editing(request, did):
    blog = get_object_or_404(Blogs, id=did)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.desc = request.POST.get('blog')
        if request.FILES.get('image'):
            blog.img = request.FILES.get('image')
        blog.save()
    return redirect('index')