from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', index, name="index"),
    path('feed/', feed, name="feed"),
    path('subscribe/', subscribe_view, name="subscribe"),
    path('detail/<int:post_id>/', post_detail, name="detail"),
    path('create/', post_create, name="create"),
    path('update/<int:post_id>/', post_update, name="update"),
    path('delete/<int:post_id>/', post_delete, name="delete"),
    path('like/<int:post_id>/', post_like, name="like"),
]