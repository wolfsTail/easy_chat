from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    """Интерфейс, благодаря которому выполняются запросы к БД"""

    def create_user(self, email, password=None):
        """Метод отвечающий за создание нового пользователя.
        Принимает email и password"""
        if not email:
            raise ValueError("Email должен быть передан!")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """Метод отвечающий за создание пользователя с правами
        администратора.
        Принимает email и password"""
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
