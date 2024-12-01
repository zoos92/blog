from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'posts', views.posts, name='posts'),
    path(r'posts/(<post_id>\d+)/', views.post, name = 'post'),
    path(r'new_post', views.new_post, name = 'new_post'),
    path(r'new_comment/(<post_id>\d+)', views.new_comment, name = 'new_comment'),
    path(r'edit_comment/(<comment_id>\d+)', views.edit_comment, name = 'edit_comment'),    
]