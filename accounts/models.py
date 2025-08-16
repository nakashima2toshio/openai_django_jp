# accounts/models.py
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# 追加、独自項目に関する加工処理などはここに書く
class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        # create_user と create_superuser の共通処理
        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):

        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'このユーザーが所属するグループ。ユーザーは、所属する各グループに付与されたすべての権限を'
            '得ることになります。'
        ),
        related_query_name="customuser",
        related_name="customuser_set",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('このユーザーのための特定の権限。'),
        related_query_name="customuser",
        related_name="customuser_set",
    )

    def __str__(self):
        return self.email
