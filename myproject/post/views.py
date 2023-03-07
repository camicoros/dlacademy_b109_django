from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from .forms import SubscribeForm, PostForm
from .models import Post


def index(request):
    posts = Post.objects.all().annotate(likes__count=Count('likes')).order_by('-likes__count')[:10]
    context = {
        "header": "All posts",
        "posts": posts,
    }
    return render(request, 'post/index.html', context)


def feed(request):
    current_user = request.user
    if current_user.is_authenticated:
        posts = Post.objects.filter(author__in=current_user.friends.all())
        header = "Your Friends's posts"
    else:
        posts = Post.objects.all()
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


def subscribe_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = SubscribeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('your_name'), form.cleaned_data.get('email'))
            return redirect('post:subscribe')

    else:
        form = SubscribeForm()

    context = {
        "header": "Subscribe",
        'form': form
    }

    return render(request, 'post/subscribe.html', context)


@login_required
def post_create(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post.get_absolute_url())

    context = {
        "header": "Create post",
        'form': form
    }
    return render(request, 'post/post_create.html', context)


def post_update(request, post_id):
    return HttpResponse(f"Update post id:{post_id}")


# class DeletePostView(DeleteView):
#     model = Post
#     pk_url_kwarg = "post_id"
#     template_name = "post/post_delete.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['header'] = f"Delete post #{self.object.id}"
#         return context
#
#     def get_success_url(self):
#         return redirect('post:index')
#
#     @method_decorator(login_required)
#     def post(self, *args, **kwargs):
#         object = self.get_object()
#
#         if self.request.user == object.author:
#             super().post(self, *args, **kwargs)
#         else:
#             return redirect('post:index')


def post_delete(request, post_id):
    return HttpResponse(f"Delete post id:{post_id}")


def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    print(request.META)

    return redirect(request.META.get('HTTP_REFERER'), request)