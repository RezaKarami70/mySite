from django import template
from blog.models import Post, Comment
from blog.models import Category
from django.utils import timezone

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    number_of_posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).count()
    return number_of_posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    comments = Comment.objects.filter(post=post, approved=True).order_by('created_date').reverse()
    return comments.count()

@register.filter()
def snippet(value,arg = 20):
    return value[:arg]

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestsposts(arg = 3):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postscategories():
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories': cat_dict}