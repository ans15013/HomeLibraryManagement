from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/new/', views.create_book, name='create_book'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('authors/', views.authors, name='authors'),
    path('authors/new/', views.create_author, name='create_author'),
    path('author/<int:author_id>/edit/', views.edit_author, name='edit_author'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('publishers/', views.publishers, name='publishers'),
    path('publishers/new/', views.create_publisher, name='create_publisher'),
    path('publisher/<int:publisher_id>/edit/', views.edit_publisher, name='edit_publisher'),
    path('publisher/<int:publisher_id>/', views.publisher, name='publisher'),
    path('series/', views.series_list, name='series_list'),
    path('series/new/', views.create_series, name='create_series'),
    path('series/<int:series_id>/edit/', views.edit_series, name='edit_series'),
    path('series/<int:series_id>/', views.series, name='series'),
    path('notes/', views.notes, name='notes'),
    path('notes/new/', views.create_note, name='create_note'),
    path('note/<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('note/<int:note_id>/', views.note, name='note'),
]
