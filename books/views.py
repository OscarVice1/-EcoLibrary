from django.shortcuts import render, get_object_or_404
from .models import Book, Favorite
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    """
    Render the home page with a list of all books.
    
    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the 'books/home.html' template with the
        context containing the list of books ordered by creation date.
    """
    books: QuerySet[Book] = Book.objects.all().order_by("publication_date")

    return render(request, "books/home.html", {"books": books})


def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    """
    Render the detail page for a specific book.

    Args:
        request (HttpRequest): The incoming HTTP request.
        book_id (int): The primary key (ID) of the book to retrieve.

    Returns:
        HttpResponse: Renders the 'books/detail.html' template with the
        requested book object. Raises Http404 if the book does not exist.
    """
    book: Book = get_object_or_404(Book, id=book_id)

    return render(request, "books/details.html", {"book": book})


def add_book_favorite()