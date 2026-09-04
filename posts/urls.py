from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.posts_view, name="posts"),
    path("create-post/", views.create_post_view, name="create_post"),
]