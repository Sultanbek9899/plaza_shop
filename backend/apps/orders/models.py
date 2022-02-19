from django.db import models

# Create your models here.
from backend.apps.products.models import Product


class Order(models.Model):
    ORDER_STATUS_NEW = 1
    ORDER_STATUS_CONFIRMED = 2
    ORDER_STATUS_SEND = 3
    ORDER_STATUS_DELIVERED = 4
    ORDER_STATUS_ARCHIVED = 5
    ORDER_STATUSES = (
        ("Новый", ORDER_STATUS_NEW),
        ("Подтвержден", ORDER_STATUS_CONFIRMED),
        ("Отправлен", ORDER_STATUS_SEND),
        ("Доставлен", ORDER_STATUS_DELIVERED),
        ("Архивирован", ORDER_STATUS_ARCHIVED),
    )

    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, null=True, blank=True)
    email = models.EmailField("Электронная почта")
    phone_number = models.CharField("номер телефона", max_length=10)
    address = models.CharField("Адрес доставки", max_length=255)
    postal_code = models.CharField("Почтовой индекс", max_length=10)
    is_paid = models.BooleanField("Оплачено",default=False, db_index=True)
    total_sum = models.DecimalField("Общая сумма",max_digits=10, decimal_places=2)
    status = models.PositiveSmallIntegerField(
        "Статус",
        choices=ORDER_STATUSES,
        db_index=True,
        default=ORDER_STATUS_NEW
    )

    created = models.DateTimeField("Создание", auto_now_add=True, db_index=True)
    updated = models.DateTimeField("Обновление", auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created']

    def __str__(self):
        return f"{self.address}-{self.first_name}-{self.phone_number}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="Товар")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return f"{self.id}"

