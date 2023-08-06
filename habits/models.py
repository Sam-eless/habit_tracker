from datetime import datetime

from django.db import models
from django.utils.timezone import now

from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class PleasantHabit(models.Model):
    PUBLIC = True
    PERSONAL = False

    STATUS = (
        (PUBLIC, 'публичная'),
        (PERSONAL, 'личная'),
    )

    title = models.CharField(max_length=150, verbose_name='Название', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кем создана', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место', **NULLABLE)
    time = models.TimeField(default="10:00")
    action = models.CharField(max_length=150, verbose_name='Действие', **NULLABLE)
    frequency = models.SmallIntegerField(default=1, verbose_name="Периодичность напоминания в днях")
    execution_time = models.TimeField(default="00:01")
    last_reminder_date = models.DateField(default=now, verbose_name="Дата последнего напоминания")
    is_public = models.BooleanField(choices=STATUS, verbose_name='Кому видна привычка', default=False)
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'

    def __str__(self):
        return f'{self.title}'


# Create your models here.
class GoodHabit(models.Model):
    PUBLIC = True
    PERSONAL = False

    STATUS = (
        (PUBLIC, 'публичная'),
        (PERSONAL, 'личная'),
    )

    title = models.CharField(max_length=150, verbose_name='Название', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кем создана', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место', **NULLABLE)
    time = models.TimeField(default="10:00", verbose_name="Время напоминания")
    action = models.CharField(max_length=150, verbose_name='Действие', **NULLABLE)
    connected_habit = models.ForeignKey(PleasantHabit, on_delete=models.CASCADE, verbose_name='Приятная привычка',
                                        **NULLABLE)
    frequency = models.SmallIntegerField(default=1, verbose_name="Периодичность напоминания в днях")
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)
    execution_time = models.TimeField(default="00:01", verbose_name='Время выполнения')
    last_reminder_date = models.DateField(default=now, verbose_name="Дата последнего напоминания")
    is_public = models.BooleanField(choices=STATUS, verbose_name='Кому видна привычка', default=False)
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'Хорошая привычка'
        verbose_name_plural = 'Хорошие привычки'

    def __str__(self):
        return f'{self.title}'
