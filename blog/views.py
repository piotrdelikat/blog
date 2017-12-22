from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'post':post})
