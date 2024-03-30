from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

from users.form import LoginForm
from .form import PostForm
from .models import Post

# Create your views here.

"""
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)
"""


def index(request):
    post_list = Post.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(Q(title__icontains=query) |
                                     Q(content__icontains=query))

    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    context = {
        'posts': post_list

    }

    return render(request, 'posts/index.html', context)


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    context = {

        'post': post
    }
    return render(request, 'posts/detail.html', context)


@login_required(login_url='/')
def create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Your Post has been SAVED successfully!....")
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)


@login_required(login_url='/')
def delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('/')


@login_required(login_url='/')
def update_view(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)
