from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Название",max_length=50)


class SubCategory(models.Model):
    name = models.CharField("Название", max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Категория")


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена",max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to="products/images/")
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
