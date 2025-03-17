from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        #Set up test data and authentication
        self.user = User.objects.create_user(username='testuser', password='')
        self.author = Author.objects.create(name='Earnest Achayo')
        self.book = Book.objects.create(title='cahayo Kingdom', publication_year=1997, author=self.author)

        self.client.login(username='testuser', password='testpassword')
    
    def test_list_books(self):
        """Test retrieving the list of books."""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book(self):
        """Test creating a book."""
        url = reverse('book-create')
        data = {"title": "The Hobbit", "publication_year": 2025, "author": self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book_detail(self):
        """Test retrieving a book by ID."""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Earnest Achay')