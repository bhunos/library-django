from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    class Meta:
        verbose_name = "User"

    def __str__(self) -> str:
        return self.name
