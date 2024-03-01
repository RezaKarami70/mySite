from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('website/latestposts.html')
def latestposts(arg):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by("published_date").reverse()[:arg]
    return {'posts': posts}