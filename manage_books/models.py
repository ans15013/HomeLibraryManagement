from django.db import models
import pytz

# Create your models here.
class Book(models.Model):
    @property
    def author(self):
        return ', '.join([f"{author.first_name} {author.last_name}" for author in self.authors.all()])
    
    COVERS = [
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
        ('ebook', 'E-book'),
        ('audiobook', 'Audiobook'),
    ]
    LANGUAGES = [
        ('english', 'English'),
        ('polish', 'Polish'),
        ('hebrew', 'Hebrew'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    cover = models.CharField(max_length=20, choices=COVERS, blank=True, null=True)
    language = models.CharField(max_length=20, choices=LANGUAGES, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    authors = models.ManyToManyField('Author', related_name='books', blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT, blank=True, null=True)
    series = models.ForeignKey('Series', on_delete=models.RESTRICT, blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    topics = models.ManyToManyField('Topic', related_name='books', blank=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    TITLES = [
        ('ks', 'Ks.'),
        ('dr', 'Dr.'),
        ('prof', 'Prof.'),
        ('bp', 'Bp.'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=50, choices=TITLES, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

class Publisher(models.Model):
    name = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=2, choices=pytz.country_names.items(), blank=True)
    founded_year = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name or "Wydawca bez nazwy"

class Genre(models.Model): #gatunek (literacki)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Series(models.Model): #seria (książek)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='series', blank=True)

    def __str__(self):
        return self.name or "Seria bez nazwy"

class Topic(models.Model): #tematyka (książki)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.book:
            return f"Notatka: {self.book.title}"
        return "Notatka bez książki"
