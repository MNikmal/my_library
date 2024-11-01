from django.db import models

class Book(models.Model):
    authors = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return(f"{self.authors}  ({self.publication_date.year})  \"{self.title}\" ISBN {self.isbn}.")

