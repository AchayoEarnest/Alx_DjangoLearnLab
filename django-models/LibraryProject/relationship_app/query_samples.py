import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
def books_by_author(author_name):
    author = Author.objects.filter(name=author_name)
    if author:
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    return []


# List all books in a library.
def books_in_library(library_name):
    library = Library.objects.get(name=library_name).first()
    if library:
        return [book.title for book in library.books.all()]
    return []




# Retrieve the librarian for a library.