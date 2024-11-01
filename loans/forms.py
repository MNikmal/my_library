from django import forms
from loans.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'title', 'publication_date', 'isbn']
        