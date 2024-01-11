from django.conf import settings
from telebot import types, TeleBot
from telebot.types import MenuButtonWebApp, WebAppInfo

from main.services.tg_user_service import TgUserService


def start(m: types.Message, bot: TeleBot):
    message = """Привет! В этом боте мы объединили 14 классных предпринимателей, которые не боятся нарушать правила и следовать за мечтой. 

Ежедневно, на протяжении 14 дней, открывайте ячейку с подарком — чтобы прокачать свои проекты, продажи и состояние. А еще внутри вас будет ждать вдохновляющая история

Нажми на кнопку Advent Calendar или меню слева, чтобы начать 

Розовый замок означает, что ячейку уже можно открыть. Нажми на него, чтобы получить подарок 

И оставь уведомления, чтобы не пропустить новый день"""

    url = "https://" + settings.MAIN_HOST + "/advent/" + str(m.chat.id) + "/"
    TgUserService.get_or_create(m)

    reply_markup = types.InlineKeyboardMarkup(row_width=1)
    reply_markup.add(
        types.InlineKeyboardButton("Advent Calеndar", web_app=WebAppInfo(url))
    )
    bot.send_message(m.chat.id, message, reply_markup=reply_markup, parse_mode='HTML')
    bot.set_chat_menu_button(chat_id=m.chat.id, menu_button=MenuButtonWebApp(text='Calendar', web_app=WebAppInfo(url), type='web_app'))
