from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


def pre(posts, target):
    list = []
    for post in posts:
        list.append(post.id)
    i = 0
    for id in list:
        if id == target.id:
            break
        i = i + 1
    if i == 0 :
        return list.__getitem__(0)
    return list.__getitem__(i-1)


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
        return list.__getitem__(i)

    return list.__getitem__(i + 1)


def blog_view(request, cat_name = None, author_username = None ):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if cat_name != None:
        posts = posts.filter(category__name = cat_name)
    if author_username != None:
        posts = posts.filter(author__username = author_username)
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
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

def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains = request.GET.get('s'))
    context = {"posts": posts}
    return render(request, 'blog/blog-home.html', context)

