from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView
from rest_framework.authtoken.views import obtain_auth_token



# Define the router and register the viewset
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

