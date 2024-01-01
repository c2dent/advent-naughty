import telebot
from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bot = telebot.TeleBot(settings.TG_BOT_TOKEN)

