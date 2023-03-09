from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', index, name="index"),
    path('feed/', feed, name="feed"),
    path('subscribe/', subscribe_view, name="subscribe"),
    path('detail/<int:post_id>/', post_detail, name="detail"),
    path('create/', post_create, name="create"),
    path('update/<int:post_id>/', UpdatePostView.as_view(), name="update"),
    path('delete/<int:post_id>/', DeletePostView.as_view(), name="delete"),
    path('comment/<int:post_id>/', post_comment, name="comment"),
    path('delete-comment/<int:comment_id>/', DeleteCommentView.as_view(), name="delete_comment"),
    path('like/<int:post_id>/', post_like, name="like"),
]