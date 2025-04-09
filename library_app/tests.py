from django.test import TestCase, Client
from rest_framework import status
from .models import Book, Member, Transaction
from django.utils import timezone

class LibraryAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test data
        self.book = Book.objects.create(name="Test Book", author="Test Author", stock=5)
        self.member = Member.objects.create(name="Test Member", debt=0)

    def test_create_book(self):
        response = self.client.post('/api/books/', {
            'name': 'New Book',
            'author': 'New Author',
            'stock': 3
        }, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_issue_book(self):
        response = self.client.post('/api/issue/', {
            'book_id': self.book.id,
            'member_id': self.member.id
        }, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.book.refresh_from_db()
        self.assertEqual(self.book.stock, 4)
        self.assertEqual(Transaction.objects.count(), 1)

    def test_return_book(self):
        # Issue the book first to decrease stock
        self.client.post('/api/issue/', {
            'book_id': self.book.id,
            'member_id': self.member.id
        }, content_type='application/json')
        
        # Check stock decreased
        self.book.refresh_from_db()
        self.assertEqual(self.book.stock, 4)  # Stock should be 5 - 1 = 4
        
        # Get the transaction (the one we just created)
        transaction = Transaction.objects.get(book=self.book, member=self.member, return_date__isnull=True)
        
        # Return the book
        response = self.client.post('/api/return/', {
            'transaction_id': transaction.id
        }, content_type='application/json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.member.refresh_from_db()
        self.assertEqual(self.book.stock, 5)  # Stock should be back to 5
        self.assertGreater(self.member.debt, 0)  # Debt should increase

    def test_search_books(self):
        response = self.client.get('/api/search/?q=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
