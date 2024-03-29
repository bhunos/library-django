from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("book_detail/<int:id>", views.book_detail, name="book_detail"),
    path(
        "create_book/",
        views.create_book,
        name="create_book",
    ),
]
