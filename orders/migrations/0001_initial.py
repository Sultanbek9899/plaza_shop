# Generated by Django 3.2.9 on 2022-02-10 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(max_length=10, verbose_name='номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес доставки')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Почтовой индекс')),
                ('is_paid', models.BooleanField(db_index=True, default=False, verbose_name='Оплачено')),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общая сумма')),
                ('status', models.PositiveSmallIntegerField(choices=[('Новый', 1), ('Подтвержден', 2), ('Отправлен', 3), ('Доставлен', 4), ('Архивирован', 5)], db_index=True, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновление')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product', verbose_name='Товар')),
            ],
        ),
    ]
