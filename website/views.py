from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse, JsonResponse
def index_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by("published_date").reverse()[:6]
    context = {'posts': posts}
    return render(request, 'website/index.html',context)

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')
