from django.shortcuts import render, get_object_or_404

from .models import Post, Group

def index(request):
    text = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'text': text
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    text = 'Записи сообщества'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'group': group,
        'text': text
    }
    return render(request, 'posts/group_post.html', context)
