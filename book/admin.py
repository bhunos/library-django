from django.contrib import admin

from .models import Books, Category, Loan

admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Loan)
