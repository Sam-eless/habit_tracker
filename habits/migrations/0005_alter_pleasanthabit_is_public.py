# Generated by Django 4.2.4 on 2023-08-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_goodhabit_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pleasanthabit',
            name='is_public',
            field=models.BooleanField(choices=[(True, 'публичная'), (False, 'личная')], default=False, verbose_name='Кому видна привычка'),
        ),
    ]