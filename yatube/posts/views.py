from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect

from yatube.settings import NUMB_PUBL

from .models import Group, Post, User

from .forms import PostForm


def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    paginator=Paginator(posts,10)
    page_number=request.GET.get('page')
    paje_obj=paginator.get_page(page_number)

    context = {
        'page_obj': paje_obj,
    }
    return render(request, 'posts/index.html', context)
    
def log_out(request):
    return render(request,'users/logged_out.html')


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUMB_PUBL]
    paginator=Paginator(posts,10)
    page_number=request.GET.get('page')
    paje_obj=paginator.get_page(page_number)
    context = {
        'page_obj':paje_obj,
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)

def profile(request,username):
    author=get_object_or_404(User,username=username)
    postsc=Post.objects.filter(author=author).count()
    posts=Post.objects.filter(author=author)
    paginator=Paginator(posts,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)


    context={
        'author':author,
        'postsc':postsc,
        'post':posts,
        'page_obj':page_obj
    }

    return render(request,'posts/profile.html',context)

def post_detail(request,post_id):
    post=Post.objects.get(pk=post_id)
    author1=post.author
    postc=Post.objects.filter(author=author1).count()


    context={
        'post':post,
        'postc':postc
    }
    return render(request,'posts/post_detail.html',context)
@login_required
def post_create(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            form.save()
            return redirect('posts:profile',request.user.username)
    groups=Group.objects.all()
    form=PostForm()
    return render(request,'posts/create_post.html',{'form':form,'groups':groups,'title1':'Добавить запись','butt':'Добавить'})

@login_required
def post_edit(request, post_id):

    post=Post.objects.get(pk=post_id)
    if request.method=='GET':
        if request.user!=post.author:
            post=Post.objects.get(pk=post_id)
            return render(request,'posts/post_detail.html',{'post':post})
        else:
            post=Post.objects.get(pk=post_id)
            form=PostForm(request.POST or None,instance=post)
            context = {
                'form': form,
                'butt':'Сохранить',
                'title1':'Редактировать запись '
            }
            return render(request,'posts/create_post.html',context)
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            form.save()
            return redirect('posts:profile',request.user.username)
    return redirect('posts:post_detail',post_id)

