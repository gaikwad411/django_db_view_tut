from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)


class BooksView(models.Model):
    book_title = models.CharField(max_length=100)
    author_first_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)

    class Meta:
        managed = False


