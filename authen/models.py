from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE
from libs.truncate_table_mixin import TruncateTableMixin


class WorkPosition(TruncateTableMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'

    def __str__(self):
        return self.name


class User(TruncateTableMixin, AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)

    patronym = models.CharField(max_length=150, blank=True, verbose_name="Отчество")
    password = models.CharField(verbose_name="password", max_length=128, **NULLABLE)
    token = models.CharField(verbose_name="Токен", **NULLABLE, max_length=100)
    worker_position = models.ForeignKey(
        to=WorkPosition,
        verbose_name="должность",
        on_delete=models.CASCADE,
        related_name='worker_positions',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('first_name', 'last_name', 'email')

    def __str__(self):
        return f"{self.first_name} {self.last_name[:1]}.{self.patronym[:1]}., {self.worker_position}"
