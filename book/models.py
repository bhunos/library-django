from datetime import date

from django.db import models

from users.models import Users


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30, blank=True, null=True)
    date_register = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Book"

    def __str__(self):
        return self.name


class Loan(models.Model):
    borrowed_name = models.CharField(max_length=30, blank=True, null=True)
    loan_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.borrowed_name
