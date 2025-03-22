from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('login/', views.home, name='login'),
    path('profile/', views.home, name='profile'),   
]