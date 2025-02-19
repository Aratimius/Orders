# Generated by Django 5.1.6 on 2025-02-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("WAITING", "В ожидании"),
                    ("READY", "Готово"),
                    ("PAID", "Оплачено"),
                ],
                default="WAITING",
                max_length=150,
                null=True,
                verbose_name="Статус заказа",
            ),
        ),
    ]
