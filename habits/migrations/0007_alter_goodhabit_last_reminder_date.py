# Generated by Django 4.2.4 on 2023-08-06 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_alter_pleasanthabit_last_reminder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodhabit',
            name='last_reminder_date',
            field=models.DateField(default=datetime.date(2023, 8, 6), verbose_name='Дата последнего напоминания'),
        ),
    ]