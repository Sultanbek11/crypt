import json

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from phone_field import PhoneField
from uuid import uuid4

from rest_framework.reverse import reverse


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class Users(AbstractUser):
    phone = PhoneField(unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа
    verify_code = models.UUIDField(default=uuid4)
    verify_code_status = models.BooleanField(null=True, default=False)

    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['username']  # Список имён полей для Superuser

    objects = MyUserManager()

    def __str__(self):
        return f'{self.email, self.verify_code}'


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE,
                                related_name='user')
    age = models.IntegerField(null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)


@receiver(post_save, sender=Users)
def create_profile(sender, instance, created, **kwargs):
    token_ = instance.verify_code
    if created:
        send_mail('krypta@gmail.com',
                  f'''
            Ваш токен: {token_}
            Пожалуйста перейдите по ссылке ниже и введите его
            http://127.0.0.1:8000/users/verify/''',
                  settings.EMAIL_HOST_USER,
                  [f'{instance.email}'],
                  fail_silently=False
                  )
        UserProfile.objects.create(user=instance)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = reset_password_token.key

    send_mail(
        "Восстановление пароля",
        f'''
        Ваш токен для восстановления пароля
        Токен: {email_plaintext_message}. 
        Перейдите по ссылке, введите ваш токен и новый пароль
        http://127.0.0.1:8000/users/password_reset/confirm/''',
        "krypta@gmail.com",
        [reset_password_token.user.email]
    )
