from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import PostModelForm

from blog.models import Post


def first_page(request):
    context = Post.objects.all()
    return render(request, 'index.html', context={'posts': context})


def add_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('first_page')
    else:
        form = PostModelForm()
    context = {'form': form}
    return render(request, 'add_post.html', context=context)


def like_post(request, id_post):
    post = get_object_or_404(Post, pk=id_post)


    post.post_likes += 1
    post.save()


    return render(request, 'check_post.html', {'posts': post})
