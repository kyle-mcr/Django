from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    context = {
        'books' : Book.objects.all(),

    }
    return render(request, "books_authors_app/index.html", context)

def authors(request):
    context = {
        'authors' : Author.objects.all(),
    }
    return render(request, "books_authors_app/authors.html", context)

def addbook_to_author(request, get_id):
    this_author = Author.objects.get(id=get_id)
    new_id = request.POST['book_id']
    this_book = Book.objects.get(id=new_id)
    this_author.books.add(this_book)
    return redirect('/authors/'+get_id)

def addauthor_to_book(request, get_id):
    this_book = Books.objects.get(id=get_id)
    new_id = request.POST['author_id']
    this_author = Author.objects.get(id=get_id)
    this_book.authors.add(this_author)
    return redirect('/books/'+get_id)

def authorsview(request, get_id):
    context = {
        'author' : Author.objects.get(id=get_id),
        'books' : Book.objects.all(),
    }
    
    return render(request, "books_authors_app/author_number.html", context)

def books(request, get_id):
    context = {
        'book' : Book.objects.get(id=get_id),
        'authors' : Author.objects.all(),
    }
    return render(request, "books_authors_app/books.html", context)

def new(request):
    if request.method=='POST':
        Book.objects.create(title=request.POST['title'], description=request.POST['desc'])
    return redirect('/')

def newa(request):
    if request.method=='POST':
        Author.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], notes=request.POST['notes'])
    return redirect('/authors')