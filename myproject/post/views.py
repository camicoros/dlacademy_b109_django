from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all().annotate(get_likes=Count('likes')).order_by('-get_likes')[:10]
    context = {
        "header": "All posts",
        "posts": posts,
    }
    return render(request, 'post/index.html', context)


def feed(request):
    current_user = request.user
    if current_user.is_authenticated:
        posts = Post.objects.filter(author__in=current_user.friends.all()).annotate(get_likes=Count('likes'))
        header = "Your Friends's posts"
    else:
        posts = Post.objects.all().annotate(get_likes=Count('likes'))
        header = "You have no friends! Find someone!"

    context = {
        "header": header,
        "posts": posts,
    }

    return render(request, 'post/feed.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    header = f"Post: {post.title}"

    # try:
    #     post = Post.objects.get(id=post_id)
    #     header = f"Post: {post.title}"
    # except Post.DoesNotExist:
    #     raise Http404("No post!")
        # post = None
        # header = "No post!"

    context = {
        "header": header,
        "post": post,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    return HttpResponse("Create post")


def post_update(request, post_id):
    return HttpResponse(f"Update post id:{post_id}")


def post_delete(request, post_id):
    return HttpResponse(f"Delete post id:{post_id}")


def post_like(request, post_id):
    return HttpResponse(f"Like post id:{post_id}")