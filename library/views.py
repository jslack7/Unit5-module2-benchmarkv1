
from django.http import JsonResponse
from .models import Member, Book


# Retrieves all books from the database
def get_all_books(request):
    # Get all books and select the fields to return
    books = Book.objects.all().values(
        "id",
        "title",
        "author",
        "checked_out_by_id"
    )

    # Convert the QuerySet into a list
    book_list = list(books)

    # Return the books as JSON
    return JsonResponse({"books": book_list})


# Retrieves books that are not checked out
def get_available_books(request):
    # Find books that have no member assigned
    books = Book.objects.filter(
        checked_out_by__isnull=True
    ).values(
        "id",
        "title",
        "author",
        "checked_out_by_id"
    )

    # Convert the QuerySet into a list
    book_list = list(books)

    # Return available books as JSON
    return JsonResponse({"books": book_list})


# Retrieves books that are currently checked out
def get_unavailable_books(request):
    # Find books that have a member assigned
    books = Book.objects.filter(
        checked_out_by__isnull=False
    ).values(
        "id",
        "title",
        "author",
        "checked_out_by_id"
    )

    # Convert the QuerySet into a list
    book_list = list(books)

    # Return unavailable books as JSON
    return JsonResponse({"books": book_list})


# Retrieves a member and their checked-out books
def get_member(request, member_id):
    try:
        # Find the member using their ID
        member = Member.objects.get(id=member_id)

        # Get books currently checked out by this member
        books = member.books.all().values(
            "id",
            "title",
            "author"
        )

        # Return the member and their books as JSON
        return JsonResponse({
            "id": member.id,
            "name": member.name,
            "email": member.email,
            "books": list(books)
        })

    except Member.DoesNotExist:
        # Return an error if the member doesn't exist
        return JsonResponse(
            {"error": "Member not found"},
            status=404
        )


# Allows a member to check out an available book
def checkout_book(request, member_id, book_id):
    try:
        # Find the member using their ID
        member = Member.objects.get(id=member_id)

        # Find the book using its ID
        book = Book.objects.get(id=book_id)

        # Check if someone already has the book
        if book.checked_out_by is not None:
            return JsonResponse(
                {"error": "Book is already checked out"},
                status=400
            )

        # Assign the book to the member
        book.checked_out_by = member

        # Save the updated book to the database
        book.save()

        # Return a successful JSON response
        return JsonResponse({
            "message": "Book checked out successfully",
            "book": book.title,
            "member": member.name
        })

    except Member.DoesNotExist:
        # Handle a member ID that doesn't exist
        return JsonResponse(
            {"error": "Member not found"},
            status=404
        )

    except Book.DoesNotExist:
        # Handle a book ID that doesn't exist
        return JsonResponse(
            {"error": "Book not found"},
            status=404
        )
