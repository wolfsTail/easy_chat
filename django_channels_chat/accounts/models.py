from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .manager import MyUserManager


class User(AbstractBaseUser):
    """Создание модели, с указанием полей определяющих пользователей:
    email, phone_number, а также служебных полей:
    is_active, is_staff, is_admin, created"""

    email = models.EmailField(max_length=250, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator(
        regex="^((\+7)|8)\d{10}$",
        message="Допустимый номер телефона должен быть \
                                введён в формате +71234567890 или \
                                81234567890",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=12, unique=True
    )
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        """Возвращает True, если у пользователя есть указанное разрешение"""
        return True

    def has_module_perms(self, app_label):
        """Возвращает True, если у пользователя есть разрешение на доступ \
            к моделям в данном приложении """
        return True
