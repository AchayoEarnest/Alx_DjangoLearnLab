## Create a Book Instance

from bookshelf.models import Book

book = Book.objects.create(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949)
print(book.id)
