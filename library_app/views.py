from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Book, Member, Transaction
from .serializers import BookSerializer, MemberSerializer, TransactionSerializer
from datetime import datetime
from django.utils import timezone

# CRUD for Books
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CRUD for Members
class MemberListCreate(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Issue a Book
@api_view(['POST'])
def issue_book(request):
    book_id = request.data.get('book_id')
    member_id = request.data.get('member_id')
    
    try:
        book = Book.objects.get(id=book_id)
        member = Member.objects.get(id=member_id)
        
        if book.stock <= 0:
            return Response({"error": "Book is out of stock"}, status=status.HTTP_400_BAD_REQUEST)
        
        if member.debt > 500:
            return Response({"error": "Member's debt exceeds KES 500"}, status=status.HTTP_400_BAD_REQUEST)
        
        book.stock -= 1
        book.save()
        
        transaction = Transaction(book=book, member=member)
        transaction.save()
        
        return Response({"message": "Book issued successfully"}, status=status.HTTP_201_CREATED)
    
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    except Member.DoesNotExist:
        return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

# Return a Book
@api_view(['POST'])
def return_book(request):
    transaction_id = request.data.get('transaction_id')
    
    try:
        transaction = Transaction.objects.get(id=transaction_id, return_date__isnull=True)
        book = transaction.book
        member = transaction.member
        
        # Calculate fee (e.g., KES 10 per day)
        days_borrowed = (timezone.now() - transaction.issue_date).days or 1
        fee = days_borrowed * 10
        
        # Update transaction
        transaction.return_date = timezone.now()
        transaction.fee = fee
        transaction.save()
        
        # Update book stock
        book.stock += 1
        book.save()
        
        # Update member debt
        member.debt += fee
        member.save()
        
        return Response({"message": "Book returned successfully", "fee": fee}, status=status.HTTP_200_OK)
    
    except Transaction.DoesNotExist:
        return Response({"error": "Transaction not found or already returned"}, status=status.HTTP_404_NOT_FOUND)

# Search Books
@api_view(['GET'])
def search_books(request):
    query = request.query_params.get('q', '')
    books = Book.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
