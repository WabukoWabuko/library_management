from django.urls import path
from .views import BookListCreate, BookDetail, MemberListCreate, MemberDetail, issue_book, return_book, search_books

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('members/', MemberListCreate.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetail.as_view(), name='member-detail'),
    path('issue/', issue_book, name='issue-book'),
    path('return/', return_book, name='return-book'),
    path('search/', search_books, name='search-books'),
]
