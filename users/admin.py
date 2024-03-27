from django.contrib import admin

from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "email", "password")
