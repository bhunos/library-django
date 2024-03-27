from django.http import HttpResponse
from django.shortcuts import redirect

from users.models import Users


def home(request):
    if request.session.get("user"):
        user = Users.objects.get(id=request.session["user"])
        return HttpResponse(f"Ola {user.name}")
    else:
        return redirect("/auth/login/?status=2")
