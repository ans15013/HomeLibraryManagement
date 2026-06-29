from django import forms

from manage_books.models import Author, Book, Note, Publisher, Series


FIELD_CLASS = "w-full p-2 border rounded"
CHECKBOX_CLASS = "h-4 w-4"


class StyledModelForm(forms.ModelForm):
    required_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.required = name in self.required_fields
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": CHECKBOX_CLASS})
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({"class": "space-y-1"})
            else:
                field.widget.attrs.update({"class": FIELD_CLASS})


class BookForm(StyledModelForm):
    required_fields = ("title",)

    class Meta:
        model = Book
        fields = [
            "title",
            "isbn",
            "publication_date",
            "pages",
            "cover",
            "language",
            "is_read",
            "is_favorite",
            "authors",
            "publisher",
            "series",
            "genres",
            "topics",
        ]
        labels = {
            "title": "Tytuł",
            "isbn": "ISBN",
            "publication_date": "Data publikacji",
            "pages": "Liczba stron",
            "cover": "Oprawa",
            "language": "Język",
            "is_read": "Przeczytana",
            "is_favorite": "Ulubiona",
            "authors": "Autorzy",
            "publisher": "Wydawca",
            "series": "Seria",
            "genres": "Gatunki",
            "topics": "Tematy",
        }
        widgets = {
            "publication_date": forms.DateInput(attrs={"type": "date"}),
            "authors": forms.CheckboxSelectMultiple,
            "genres": forms.CheckboxSelectMultiple,
            "topics": forms.CheckboxSelectMultiple,
        }


class AuthorForm(StyledModelForm):
    required_fields = ("first_name", "last_name")

    class Meta:
        model = Author
        fields = ["first_name", "last_name", "alias", "nationality", "title"]
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "alias": "Pseudonim",
            "nationality": "Narodowość",
            "title": "Tytuł",
        }


class PublisherForm(StyledModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "country", "founded_year", "website", "email"]
        labels = {
            "name": "Nazwa",
            "country": "Kraj",
            "founded_year": "Rok założenia",
            "website": "Strona WWW",
            "email": "E-mail",
        }


class SeriesForm(StyledModelForm):
    class Meta:
        model = Series
        fields = ["name", "description", "authors"]
        labels = {
            "name": "Nazwa",
            "description": "Opis",
            "authors": "Autorzy",
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "authors": forms.CheckboxSelectMultiple,
        }


class NoteForm(StyledModelForm):
    class Meta:
        model = Note
        fields = ["book", "content"]
        labels = {
            "book": "Książka",
            "content": "Treść notatki",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5}),
        }
