from django.shortcuts import get_object_or_404, render

from yatube.settings import NUMB_PUBL

from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUMB_PUBL]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUMB_PUBL]
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)
