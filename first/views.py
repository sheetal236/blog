from django.shortcuts import render
from django.utils import timezone
from .models import post

def post_list(request):
    posts=post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'first/post_list.html', {'posts': posts})


