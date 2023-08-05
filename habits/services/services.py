from datetime import date, timedelta, datetime

from django.core.mail import send_mail

from config import settings
from habits.models import GoodHabit
from users.models import User


def checking_habit():
    habits = GoodHabit.objects.all()

    for habit in habits:
        if date.today() == habit.last_reminder_date + timedelta(days=habit.frequency):
            datetime_habit_time = datetime.combine(date.today(), habit.time)
            date_time_difference = datetime.now() - datetime_habit_time
            # print(date_time_difference.total_seconds())
            if -120 < date_time_difference.total_seconds() < 120:
                print('Необходимо напомнить о привычке в телегу, пиу пиу')
