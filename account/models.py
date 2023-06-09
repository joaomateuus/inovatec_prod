from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from account import managers

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30,
        unique=True
    )
    nome = models.CharField(
        'Nome',
        max_length=50,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        unique=True
    )
    cpf = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    numero_telefone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    is_fiscal = models.BooleanField(
        null=True,
        blank=True,
    )
    joined_in = models.DateField(
        auto_now_add=True,
        editable=False,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=True
    )
    last_login = models.DateTimeField(
        null=True
    )
    is_staff = models.BooleanField(
        null=True,
        default=False
    )
    is_superuser = models.BooleanField(
        null=True,
        default=False
    )
    
    objects = managers.UsersManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nome', 'cpf', 'is_fiscal']
     
    class Meta:
        db_table = 'tb_usuarios'
