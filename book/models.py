from datetime import date

from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30, blank=True, null=True)
    date_register = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    borrowed_name = models.CharField(max_length=30, blank=True, null=True)
    loan_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    duration_time = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Book'

    def __str__(self):
        return self.name
