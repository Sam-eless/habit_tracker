# Generated by Django 4.2.4 on 2023-08-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_goodhabit_is_public_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodhabit',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Видна всем'),
        ),
        migrations.AlterField(
            model_name='pleasanthabit',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Видна всем'),
        ),
    ]