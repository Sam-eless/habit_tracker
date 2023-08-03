from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    tg_login = models.CharField(max_length=100, verbose_name='логин пользователя в телеграм')
    tg_chat_id = models.CharField(max_length=100, verbose_name='id чата в телеграм')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    # avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    is_email_verified = models.BooleanField(verbose_name='email подтвержден', default=False)
    # is_blocked = models.BooleanField(verbose_name='пользователь заблокирован', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
