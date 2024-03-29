from hashlib import sha256

from django.shortcuts import render, redirect

from .models import Users


def login(request):
    if request.session.get("user"):
        return redirect("/book/home")
    status = request.GET.get("status")
    return render(request, "login.html", {"status": status})


def register(request):
    if request.session.get("user"):
        return redirect("/book/home")
    status = request.GET.get("status")
    return render(request, "register.html", {"status": status})


def validate_registration(request):
    name = request.POST.get("name").strip()
    email = request.POST.get("email").strip()
    password = request.POST.get("password")

    users = Users.objects.filter(email=email)

    if len(name) == 0 or len(email) == 0:
        return redirect("/auth/register/?status=1")

    if len(password) < 8:
        return redirect("/auth/register/?status=2")

    if len(users) > 0:
        return redirect("/auth/register/?status=3")

    try:
        password = sha256(password.encode()).hexdigest()
        users = Users(name=name, email=email, password=password)
        users.save()

        return redirect("/auth/login/?status=0")
    except Exception as e:
        print("Erro ao criar usuario: {}".format(e))
        return redirect("/auth/register/?status=4")


def validate_login(request):
    email = request.POST.get("email").strip()
    password = sha256(request.POST.get("password").encode()).hexdigest()

    user = Users.objects.filter(email=email).filter(password=password)

    if len(user) == 0:
        return redirect("/auth/login/?status=1")
    elif len(user) > 0:
        request.session["user"] = user[0].id
        return redirect("/book/home")


def logout(request):
    request.session.flush()
    return redirect("/auth/login/")
