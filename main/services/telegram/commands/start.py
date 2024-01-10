from django.conf import settings
from telebot import types, TeleBot
from telebot.types import MenuButtonWebApp, WebAppInfo

from main.services.tg_user_service import TgUserService


def start(m: types.Message, bot: TeleBot):
    message = """<strong>Что умеет этот бот?</strong>
Привет! В этом боте мы объединили 14 классных предпринимателей, которые не боятся нарушать правила и следовать за мечтой. 

Санта для таких «плохишей» (naughty list) оставил бы только уголёк, поэтому мы решили сами собрать мешок подарков и подарить вам, если вы тоже любите экспериментировать, как наши герои. 

Ежедневно, на протяжении 14 дней, вы будете получать по одной поучительной или вдохновляющей истории. Все они основаны на реальных событиях и связаны с «внутрянкой» развития бизнеса, о которой никто обычно не говорит 🤫

Скорее открывайте адвент-календарь и оставьте уведомления включёнными. Вам точно будет интересно 😏"""

    url = "https://" + settings.MAIN_HOST + "/advent/" + str(m.chat.id) + "/"
    TgUserService.get_or_create(m)

    reply_markup = types.InlineKeyboardMarkup(row_width=1)
    reply_markup.add(
        types.InlineKeyboardButton("Advent Calеndar", web_app=WebAppInfo(url))
    )
    bot.send_message(m.chat.id, message, reply_markup=reply_markup, parse_mode='HTML')
    bot.set_chat_menu_button(chat_id=m.chat.id, menu_button=MenuButtonWebApp(text='Calendar', web_app=WebAppInfo(url), type='web_app'))
