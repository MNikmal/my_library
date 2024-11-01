from faker import Faker
from loans.models import Book

fake = Faker()

for i in range(100):
    author = f"{fake.last_name()}, {fake.first_name()}"
    title = fake.sentence()
    publication_date = fake.date()
    isbn = fake.unique.isbn13().replace('-','')
    
    Book.objects.create(authors=author, title=title, publication_date=publication_date, isbn=isbn)