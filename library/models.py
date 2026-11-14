from django.db import models

# Represents a library member
class Member(models.Model):

    # Stores the member's name
    name = models.CharField(max_length=100)

    # Stores a unique email address
    email = models.EmailField(unique=True)

    # Displays the member's name
    def __str__(self):
        return self.name


# Represents a book in the library
class Book(models.Model):

    # Stores the book's title
    title = models.CharField(max_length=200)

    # Stores the author's name
    author = models.CharField(max_length=100)

    # Connects the book to its current borrower
    checked_out_by = models.ForeignKey(
        Member,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books"
    )

    # Displays the book's title
    def __str__(self):
        return self.title