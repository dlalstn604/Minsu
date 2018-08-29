from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def my_game(request):
    return render(request, 'blog/my_game.html')

def clock(request):
    return render(request, 'blog/clock.html')

def image(request):
    return render(request, 'blog/image.html')