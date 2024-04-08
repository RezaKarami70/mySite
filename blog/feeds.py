from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "blog latest posts"
    link = "/rss/feed"
    description = "Updates on changes and additions to bog."

    def items(self):
        return Post.objects.filter(status=True).order_by("published_date").reverse()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:10]