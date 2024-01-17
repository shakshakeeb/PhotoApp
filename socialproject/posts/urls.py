from django.urls import path
from . import views

# URL patterns for the 'posts' app
urlpatterns = [
    # URL pattern for creating a new post, post feed and like
    path('create', views.post_create, name='create'),
    path('feed', views.feed, name='feed'),
    path('like', views.like_post, name='like'),
]
