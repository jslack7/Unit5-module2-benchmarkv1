
from django.urls import path
from . import views


urlpatterns = [
    # Retrieves all books
    path("books/", views.get_all_books, name="get_all_books"),

    # Retrieves available books
    path(
        "books/available/",
        views.get_available_books,
        name="get_available_books"
    ),

    # Retrieves unavailable books
    path(
        "books/unavailable/",
        views.get_unavailable_books,
        name="get_unavailable_books"
    ),

    # Retrieves a member and their checked-out books
    path(
        "members/<int:member_id>/",
        views.get_member,
        name="get_member"
    ),

    # Allows a member to check out a book
    path(
        "checkout/<int:member_id>/<int:book_id>/",
        views.checkout_book,
        name="checkout_book"
    ),
]
