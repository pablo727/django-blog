"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a single blog topic.
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    # Page for adding a new topic.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for adding a new post.
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # Page for editing a new post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]