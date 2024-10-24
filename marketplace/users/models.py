from django.db import models
from django.core.validators import RegexValidator
from .validators import validate_password
from django.contrib.auth.hashers import make_password
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)  # Обязательно
    birth_date = models.DateField(blank=False, null=False)  # Обязательно
    phone_number = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^(?:\+7|8)\d{10}$",
                message="Номер телефона должен начинаться с +7 или 8 и содержать всего 11 цифр.",
            )
        ],
        blank=False,
        null=False,  # Обязательно
    )
    city = models.CharField(max_length=255, blank=False, null=False)  # Обязательно
    total_spent = models.DecimalField(
        max_digits=20, decimal_places=2, default=0, blank=True, null=False
    )  # Не обязательно
    purchase_to_return_ratio = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, blank=True, null=False
    )  # Не обязательно



    def update_total_spent(self, amount):
        """Обновление суммы выкупа"""
        self.total_spent += amount
        self.save(update_fields=["total_spent"])

    def update_purchase_to_return_ratio(self, purchases, returns):
        """
        Обновляет процент выкупа на основе количества покупок и возвратов.
        :param purchases: Количество покупок
        :param returns: Количество возвратов
        """
        if purchases == 0:
            self.purchase_to_return_ratio = 0
        else:
            self.purchase_to_return_ratio = (purchases - returns) / purchases * 100

        self.save(update_fields=["purchase_to_return_ratio"])


class Admin(models.Model):
    email = models.EmailField(unique=True,  blank=False, null=False)  # Электронная почта администратора
    password = models.CharField(
        max_length=50, validators=[validate_password],  blank=False, null=False  # Валидация по кастомным правилам
    )  # Пароль администратора
    access_rights = models.JSONField()  # Права доступа

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
