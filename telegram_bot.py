import os
import django
import telebot
from telebot import types

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from config import settings
from users.models import User

if __name__ == '__main__':
    bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)


    @bot.message_handler(commands=['start'])
    def start(message):
        tg_login = f'@{message.from_user.username}'
        try:
            user = User.objects.get(tg_login=tg_login)
            if user:
                user.tg_chat_id = message.chat.id
                user.save()

                message_data = {
                    message.chat.id,
                    f'Привет {message.from_user.username}, теперь ты будешь получать уведомления о своих привычках в телеграм!'
                }
                bot.send_message(*message_data)

            else:
                message_data = {
                    message.chat.id,
                    f'Привет {message.from_user.username}, в моей системе нет твоего логина, я не смогу присылать тебе уведомления о своих привычках в телеграм :('
                }
                bot.send_message(*message_data)

        except User.DoesNotExist:
            message_data = {
                message.chat.id,
                f'Привет {message.from_user.username}, в моей системе нет твоего логина, я не смогу присылать тебе уведомления о своих привычках в телеграм :('
            }
            bot.send_message(*message_data)


    bot.polling(none_stop=True)
