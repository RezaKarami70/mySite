from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from website.forms import newsletterForm
from blog.forms import CommentForm
from django.contrib import messages


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


def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if  kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your Comment submited successfully')
        else:
            messages.add_message(request,messages.WARNING,'your Comment did not submited successfully')
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(post=post, approved=True).order_by('created_date').reverse()
    p = posts.get(id = pre(posts, post))
    n = posts.get(id = next(posts, post))
    post.counted_views += 1
    post.save()
    form = CommentForm()
    context = {"post": post,'comments':comments , "pre": p, "next": n, 'form': form}
    
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains = request.GET.get('s'))
    context = {"posts": posts}
    return render(request, 'blog/blog-home.html', context)


def newsletter_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if  kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {"posts": posts}

    if request.method == 'POST':
        form = newsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/blog-home.html', context)
    else:        
        return render(request, 'blog/blog-home.html', context)