from django.urls import path, re_path
from .views import index1, index2

urlpatterns = [
    path('python/', index1),
    path('html/', index2)
]