from django.db import models

# Create your models here.
class Book(models.Model):
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


    title = models.Charfield(max_lenght=200)
    isbn = models.Charfield(max_lenght=20, unique=True)
    publication_date = models.DataField()
    pages = models.IntegerField()
    cover = models.CharFiled(max_lenght=20)
    language = models.CharField(max_lenght=20)
    is_read = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)


class Author(models.Model):

class Publisher(models.Model):

class Genre(models.Model):

class Series(models.Model):

class Topic(models.Model):

class Category(models.Model):

class Note(models.Model):