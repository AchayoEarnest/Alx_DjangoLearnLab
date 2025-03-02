from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm  # Import the form

@login_required
@permission_required('bookshelf.view_book', raise_exception=True)  # Corrected permission
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@permission_required('bookshelf.add_book', raise_exception=True)  # Corrected permission
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    
    return render(request, "bookshelf/book_form.html", {"form": form})

@login_required
@permission_required('bookshelf.change_book', raise_exception=True)  # Corrected permission
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    
    return render(request, "bookshelf/book_form.html", {"form": form})

@login_required
@permission_required('bookshelf.delete_book', raise_exception=True)  # Corrected permission
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":  # To confirm deletion via a POST request
        book.delete()
        return redirect("book_list")
    
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
