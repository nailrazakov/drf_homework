from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from college.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    town = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите из какого города",
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        blank=True,
        null=True,
        verbose_name="Аватарка",
        help_text="Загрузите аватарку",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    CASH = 'cash'
    NON_CASH = 'non_cash'
    PAY_METHOD_CHOOSES = (
        (CASH, 'наличные'),
        (NON_CASH, 'перевод на счет')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата платежа")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    amount = models.IntegerField(verbose_name="Сумма оплаты")
    method = models.TextField(
        max_length=15, choices=PAY_METHOD_CHOOSES, default="не выбрано"
    )

    def __str__(self):
        return f"Платеж {self.amount} руб. {self.method}\n{self.user} {self.course} {self.lesson}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
