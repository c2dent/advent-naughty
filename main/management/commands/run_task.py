import time

import telebot
from django.conf import settings
from django.core.management import BaseCommand

from main.tasks import send_planned_messages


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bot = telebot.TeleBot(settings.TG_BOT_TOKEN)
        launched = True
        try:
            print('Запуск задачи')
            while launched:
                try:
                    send_planned_messages(bot)
                    time.sleep(60)
                except Exception as e:
                    print(e)
                    launched = False
        except KeyboardInterrupt:
            print("Остановка задачи...")
