from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import register
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView,
    PostDeleteView, MyPostsView,CustomLoginView,CustomLogoutView,
    PostDetailAPIView, PostListAPIView, RegisterAPIView,LoginAPIView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('my-posts/', MyPostsView.as_view(), name='my_posts'),
    path('login/', CustomLoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list_create'),
    path('api/posts/<slug:slug>/', PostDetailAPIView.as_view(), name='api_post_detail'),
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/login/', LoginAPIView.as_view(), name='api_login'),

]
