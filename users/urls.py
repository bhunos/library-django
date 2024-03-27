from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path(
        "validate_registration/",
        views.validate_registration,
        name="validate_registration",
    ),
    path(
        "validate_login/",
        views.validate_login,
        name="validate_login",
    ),
    path("logout/", views.logout, name="logout"),
]
