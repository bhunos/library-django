from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("book_detail/<int:id>", views.book_detail, name="book_detail"),
]
