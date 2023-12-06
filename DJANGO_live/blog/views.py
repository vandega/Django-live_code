from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post


def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all().filter(published=True)
        context = {'posts': posts}
        return render(request, 'blog/blogs.html', context=context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_posts')
        else:
            print(form.errors)
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'blog/create_post.html', context=context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/delete_post.html', context=context)

    elif request.method == 'POST':

        post.delete()
        return redirect('all_posts')


def post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_page.html', context=context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {'form': form, 'post': post}
    return render(request, 'blog/create_post.html', context=context)
