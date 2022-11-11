from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    login = models.CharField(max_length=15, null=False)
    password = models.CharField(null=False, max_length=50)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.login
