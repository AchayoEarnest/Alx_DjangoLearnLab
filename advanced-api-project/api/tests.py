from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='earnest', password='user1234')
        self.author = Author.objects.create(name='Earnest Achayo')
        self.book = Book.objects.create(title='Cahayo Empire Kingdom', publication_year=2025, author=self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Cahayo Empire Kingdom')
        self.assertEqual(self.book.publication_year, 2025)
        self.assertEqual(self.book.author.name, 'Earnest Achayo')
