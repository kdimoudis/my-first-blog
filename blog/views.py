from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category, Composer, Label
from .forms import PostForm
from django.shortcuts import redirect


def post_start(request):
    return render(request, 'blog/post_start.html')   

def post_list(request):
    cat=request.GET.get('cat','')
    try:
        cat=int(cat)
    except:
        cat=False

    if (cat==False):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list2(request):
    lab=request.GET.get('lab','')
    try:
        lab=int(lab)
    except:
        lab=False

    if (lab==False):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).filter(label=lab).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})    

def post_list3(request):
    comp=request.GET.get('comp','')
    try:
        comp=int(comp)
    except:
        comp=False

    if (comp==False):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).filter(composer=comp).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')