from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MyFriend, Post
from django.utils import timezone
from .forms import PostForm

def memo_index(request):
    return render(request, 'sungsani/memo_index.html', {})

def index2(request):
    asdf = MyFriend.a
    aa = MyFriend.b
    context = {"asdf":asdf, "aa":aa}
    return render(request, 'sungsani/index.html', context)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {"posts":posts}
    return render(request, 'sungsani/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'sungsani/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(to='sungsani:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'sungsani/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.revised_date = timezone.now()
            post.save()
            return redirect('sungsani:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sungsani/post_new.html', {'form': form})
# Create your views here.
