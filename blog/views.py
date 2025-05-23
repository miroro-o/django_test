from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    print("View вызвана")
    posts = Post.objects.all()
    print("Шаблон:", 'blog/post_list.html')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})