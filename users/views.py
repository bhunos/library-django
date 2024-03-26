from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("login")


def register(request):
    return render(request, "register.html")
