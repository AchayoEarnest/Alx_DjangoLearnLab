from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', PostListView.as_view(), name='posts'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.Profile, name='profile'),  
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),   
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', views.add_comment, name='add_comment'),
    path('comments/<int:pk>/update/', views.edit_comment, name='edit_comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]