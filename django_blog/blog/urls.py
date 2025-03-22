from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', views.home, name='login'),
    path('profile/', views.home, name='profile'),  
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),   
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),  
]