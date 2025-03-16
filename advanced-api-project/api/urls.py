from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateView, BookDetailView
from rest_framework.authtoken.views import obtain_auth_token



# Define the router and register the viewset
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
