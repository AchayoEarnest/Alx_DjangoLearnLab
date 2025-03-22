from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('login/', views.home, name='login'),
    path('profile/', views.home, name='profile'),   
]