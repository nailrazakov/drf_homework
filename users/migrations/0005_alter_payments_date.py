# Generated by Django 5.0.4 on 2024-05-11 10:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_payments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата платежа'),
        ),
    ]
