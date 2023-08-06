from datetime import date, timedelta, datetime
import requests
from rest_framework.response import Response
from config import settings
from habits.models import GoodHabit, PleasantHabit
from users.models import User


def checking_good_habit():
    habits = GoodHabit.objects.all()
    for habit in habits:
        if date.today() == habit.last_reminder_date + timedelta(days=habit.frequency):
            datetime_habit_time = datetime.combine(date.today(), habit.time)
            datetime_difference = datetime.now() - datetime_habit_time
            if -300 < datetime_difference.total_seconds() < -200:
                print('Необходимо напомнить о привычке в телегу, пиу пиу')
                if habit.user.tg_chat_id is not None:
                    habit.last_reminder_date = date.today()
                    habit.save()

                    if habit.reward is not None:
                        reward = habit.reward
                    else:
                        reward = habit.connected_habit

                    request_data = {
                        "chat_id": habit.user.tg_chat_id,
                        "text": f"Привет {habit.user.tg_login}! Напоминаю, что на [ {habit.time} ]"
                                f" у тебя запланировано [ {habit.action} ] в [ {habit.place} ], тебе потребуется около "
                                f"[ {habit.execution_time.minute} ] минут. После выполнения тебя ждет [ {reward} ] :) \n"
                                f"[ Полезная привычка ]"
                    }
                    response = requests.post(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage',
                                             request_data)
                    return Response(response.json())
                else:
                    print(f' Невозможно отправить сообщение, пользователь {habit.user.email} '
                          f'не авторизован в телеграм боте, tg_chat_id is None')


def checking_pleasant_habit():
    habits = PleasantHabit.objects.all()
    for habit in habits:
        if date.today() == habit.last_reminder_date + timedelta(days=habit.frequency):
            datetime_habit_time = datetime.combine(date.today(), habit.time)
            datetime_difference = datetime.now() - datetime_habit_time
            if -300 < datetime_difference.total_seconds() < -200:
                print('Необходимо напомнить о привычке в телегу, пиу пиу')
                if habit.user.tg_chat_id is not None:
                    habit.last_reminder_date = date.today()
                    habit.save()
                    request_data = {
                        "chat_id": habit.user.tg_chat_id,
                        "text": f"Привет {habit.user.tg_login}! Напоминаю, что на [ {habit.time} ]"
                                f" у тебя запланировано [ {habit.action} ] в [ {habit.place} ], тебе потребуется около "
                                f"[ {habit.execution_time.minute} ] минут. \n"
                                f"[ Приятная привычка ]"
                    }
                    response = requests.post(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage',
                                             request_data)
                    return Response(response.json())
                else:
                    print(f' Невозможно отправить сообщение, пользователь {habit.user.email} '
                          f'не авторизован в телеграм боте, tg_chat_id is None')
