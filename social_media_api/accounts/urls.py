from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomAuthToken 
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)  

urlpatterns = [
    path('api/', include(router.urls)),  
    path('api/login/', CustomAuthToken.as_view(), name='login'),
    path('api/register/', views.register, name='register'), 
    path('api/profile/', views.profile, name='profile'), 
]