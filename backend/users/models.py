from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole:
    ADMIN = 'admin'
    FORECASTER = 'forecaster'
    USER = 'user'
    
    
    choices = [
        (ADMIN, 'ADMIN'),
        (FORECASTER, 'FORECASTER'),
        (USER, 'USER'),
    ]


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Username')
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Email')
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='First name')
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Last name')
    role = models.TextField(
        choices=UserRole.choices,
        default=UserRole.USER,
        verbose_name='User role')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN or self.is_superuser
    
    @property
    def is_forecaster(self):
        return self.role == UserRole.FORECASTER

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username']

    def __str__(self):
        return self.username
