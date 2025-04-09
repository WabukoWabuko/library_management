from django.db import models
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} by {self.author}"

class Member(models.Model):
    name = models.CharField(max_length=100)
    debt = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    fee = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.book.name} issued to {self.member.name}"
