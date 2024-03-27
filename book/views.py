from django.shortcuts import redirect, render

from users.models import Users
from .models import Books


def home(request):
    if request.session.get("user"):
        user = Users.objects.get(id=request.session["user"])
        books = Books.objects.filter(userId=user.id)
        return render(request, "home.html", {"user": user, "books": books})
    else:
        return redirect("/auth/login/?status=2")


def book_detail(request, id):
    if request.session.get("user"):
        book = Books.objects.get(id=id)
        if request.session.get("user") == book.userId.id:
            return render(request, "book_detail.html", {"book": book})
        else:
            return redirect("/auth/home")

    return redirect("/auth/login/?status=2")
