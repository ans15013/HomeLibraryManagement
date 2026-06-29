from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from manage_books.forms import AuthorForm, BookForm, NoteForm, PublisherForm, SeriesForm
from manage_books.models import Book, Author, Publisher, Series, Note

def index(request):
    books = Book.objects.all()
    return render(request, 'manage_books/index.html.jinja', {'books': books})

def book(request, book_id):
    return render(request, 'manage_books/book.html.jinja', {'book_id': book_id})

def author(request, author_id):
    return render(request, 'manage_books/author.html.jinja', {'author_id': author_id})

def publisher(request, publisher_id):
    return render(request, 'manage_books/publisher.html.jinja', {'publisher_id': publisher_id})

def series(request, series_id):
    return render(request, 'manage_books/series.html.jinja', {'series_id': series_id})

def note(request, note_id):
    return render(request, 'manage_books/note.html.jinja', {'note_id': note_id})

def authors(request):
    authors = Author.objects.all()
    return render(request, 'manage_books/authors.html.jinja', {'authors': authors})

def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'manage_books/publishers.html.jinja', {'publishers': publishers})

def series_list(request):
    series = Series.objects.all()
    return render(request, 'manage_books/series_list.html.jinja', {'series': series})

def notes(request):
    notes = Note.objects.all()
    return render(request, 'manage_books/notes.html.jinja', {'notes': notes})

def create_book(request):
    form = BookForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Dodaj książkę',
        'submit_label': 'Zapisz książkę',
        'cancel_url': 'index',
    })

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Edytuj książkę',
        'submit_label': 'Zapisz zmiany',
        'cancel_url': 'index',
    })

def create_author(request):
    form = AuthorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('authors')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Dodaj autora',
        'submit_label': 'Zapisz autora',
        'cancel_url': 'authors',
    })

def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    form = AuthorForm(request.POST or None, instance=author)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('authors')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Edytuj autora',
        'submit_label': 'Zapisz zmiany',
        'cancel_url': 'authors',
    })

def create_publisher(request):
    form = PublisherForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('publishers')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Dodaj wydawcę',
        'submit_label': 'Zapisz wydawcę',
        'cancel_url': 'publishers',
    })

def edit_publisher(request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id)
    form = PublisherForm(request.POST or None, instance=publisher)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('publishers')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Edytuj wydawcę',
        'submit_label': 'Zapisz zmiany',
        'cancel_url': 'publishers',
    })

def create_series(request):
    form = SeriesForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('series_list')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Dodaj serię',
        'submit_label': 'Zapisz serię',
        'cancel_url': 'series_list',
    })

def edit_series(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    form = SeriesForm(request.POST or None, instance=series)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('series_list')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Edytuj serię',
        'submit_label': 'Zapisz zmiany',
        'cancel_url': 'series_list',
    })

def create_note(request):
    form = NoteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('notes')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Dodaj notatkę',
        'submit_label': 'Zapisz notatkę',
        'cancel_url': 'notes',
    })

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    form = NoteForm(request.POST or None, instance=note)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('notes')
    return render(request, 'manage_books/form.html.jinja', {
        'form': form,
        'title': 'Edytuj notatkę',
        'submit_label': 'Zapisz zmiany',
        'cancel_url': 'notes',
    })
