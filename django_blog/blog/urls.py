from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', PostListView.as_view(), name='posts'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),  
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),   
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
]