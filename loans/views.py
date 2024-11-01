from django.shortcuts import redirect, render
from django.http import Http404
import random

from loans.models import Book
from loans.forms import BookForm


def welcome(request):
    slogans = ["Having fun isn't hard when you've got a library card.", "Libraries make shhh happen.", "Believe in your shelf.",
    "Need a good read? We've got you covered.", "Check us out. And maybe one of your books too.", "Get a better read on the world."]
    slogan = random.choice(slogans)

    context = {'slogan': slogan}
    return render(request, 'welcome.html', context)


def books(request):
    books = Book.objects.all()
    print(books)
    context = {'books': books}
    return render(request, 'books.html', context)


def get_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except(Book.DoesNotExist):
        raise Http404(f"Could not find book with primary key {book_id}")

    context = {'book': book}
    return render(request, 'book.html', context)


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, "It was not possible to save this book in the database.")
            else:
                return redirect('/books/')
    else:
        form = BookForm()

    return render(request, 'create_book.html', {'form': form})


def update_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except(Book.DoesNotExist):
        raise Http404(f"Could not find book with primary key {book_id}")
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, "It was not possible to update this book in the database.")
            else:
                return redirect('/books/')
    else:
        form = BookForm(instance=book)

    context = {'book': book, 'form': form}
    return render(request, 'update_book.html', context)


def delete_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except(Book.DoesNotExist):
        raise Http404(f"Could not find book with primary key {book_id}")
    
    if request.method == 'POST':
        book.delete()
        return redirect('/books/')

    return render(request, 'delete_book.html', {'book': book})