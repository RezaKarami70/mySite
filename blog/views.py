from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def pre(posts, target):
    list = []
    for post in posts:
        list.append(post.id)
    i = 0
    for id in list:
        if id == target.id:
            break
        i = i + 1
    return list.__getitem__(i - 1)

    



def next(posts, target):
    list = []
    for post in posts:
        list.append(post.id)
    i = 0
    for id in list:
        if id == target.id:
            break
        i = i + 1

    if i >= list.__len__()-1:
        i = -1

    return list.__getitem__(i + 1)



def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {"posts": posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    post = get_object_or_404(posts, pk=pid)
    p = posts.get(id = pre(posts, post))
    n = posts.get(id = next(posts, post))
    post.counted_views += 1
    post.save()
    context = {"post": post, "pre": p, "next": n}
    return render(request, 'blog/blog-single.html', context)
