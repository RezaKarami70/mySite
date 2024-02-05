from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime

def blog_view(request):
    posts = Post.objects.filter(published_date__lte = datetime.now() , status = 1)
    context = {"posts": posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    post.counted_views += 1
    post.save()
    context = {"post": post}
    return render(request, 'blog/blog-single.html',context)
