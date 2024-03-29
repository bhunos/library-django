from django.shortcuts import redirect, render, get_object_or_404

from .models import Users, Books, Category, Loan


def home(request):
    if request.session.get("user"):
        user = Users.objects.get(id=request.session["user"])
        books = Books.objects.filter(user=user.id)
        category_book = Category.objects.filter(user_id=request.session.get("user"))

        return render(
            request,
            "home.html",
            {
                "user": user,
                "books": books,
                "category_book": category_book,
                "session": request.session.get("user"),
            },
        )
    else:
        return redirect("/auth/login/?status=2")


def book_detail(request, id):
    if request.session.get("user"):
        book = Books.objects.get(id=id)
        if request.session.get("user") == book.user.id:
            category_book = Category.objects.filter(user_id=request.session.get("user"))
            loan = Loan.objects.filter(book_id=book.id)

            def square(row):
                if row.loan_date and row.return_date:
                    return (row.return_date - row.loan_date) // 3600
                else:
                    return None

            return render(
                request,
                "book_detail.html",
                {
                    "book": {
                        "name": book.name,
                        "author": book.author,
                        "co_author": book.co_author if book.co_author else "",
                        "date_register": book.date_register.strftime("%Y-%m-%d"),
                        "borrowed": book.borrowed,
                        "category": book.category,
                        "user": book.user,
                    },
                    "category_book": category_book,
                    "loan": [
                        {
                            "borrowed_name": row.borrowed_name,
                            "loan_date": row.loan_date if row.loan_date else "-",
                            "return_date": row.return_date if row.return_date else "-",
                            "book": row.book,
                            "date_difference": (
                                (row.return_date - row.loan_date).days
                                if row.loan_date and row.return_date
                                else "-"
                            ),
                        }
                        for row in loan
                    ],
                    "session": request.session.get("user"),
                },
            )
        else:
            return redirect("/auth/home")

    return redirect("/auth/login/?status=2")


def create_book(request):
    if request.method == "POST" and request.session.get("user"):
        name = request.POST.get("name")
        author = request.POST.get("author")
        co_author = request.POST.get("co_author")
        date_register = request.POST.get("date_register")
        borrowed = request.POST.get("borrowed") == "on" if True else False
        category = request.POST.get("category")
        user = request.session.get("user")

        category = get_object_or_404(Category, id=category)
        user = get_object_or_404(Users, id=user)

        try:
            book = Books(
                name=name,
                author=author,
                co_author=co_author,
                date_register=date_register,
                borrowed=borrowed,
                category=category,
                user=user,
            )

            book.save()
            return redirect("/book/home/?status=2")
        except Exception as e:
            print("Erro ao salvar o livro: {}".format(e))
            return redirect("/book/home/?status=4")
    else:
        return redirect("/book/home/?status=2")
