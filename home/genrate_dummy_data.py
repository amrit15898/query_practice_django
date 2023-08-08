from django.db import models
from faker import Faker
from django.utils import timezone
from .models import  *
fake = Faker()

def create_genres(num_genres=5):
    genres = [Genre(name=fake.word()) for _ in range(num_genres)]
    Genre.objects.bulk_create(genres)

def create_authors(num_authors=10):
    authors = [Author(name=fake.name(), birth_date=fake.date_of_birth()) for _ in range(num_authors)]
    Author.objects.bulk_create(authors)

def create_books(num_books=50):
    genres = Genre.objects.all()
    authors = Author.objects.all()
    books = [
        Book(
            title=fake.catch_phrase(),
            author=authors[fake.random_int(0, len(authors) - 1)],
            genre=genres[fake.random_int(0, len(genres) - 1)],
            publication_date=fake.date_this_decade(),
        )
        for _ in range(num_books)
    ]
    Book.objects.bulk_create(books)
