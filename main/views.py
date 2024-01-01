import html
import json
import textwrap

import telebot
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from telebot.types import InputMediaPhoto

from main.models import TgUser, UserCell, Cell
from main.models.cell_message_image import CellMessageImage
from main.seriazlizers.user_cell_serializer import UserCellSerializer
from main.services.tg_user_service import TgUserService


def advent(request, user_id):
    user_exists = TgUser.objects.filter(user_id=user_id).exists()
    if user_exists is False:
        return render(request, '404.html', {}, status=404)

    user = TgUser.objects.filter(user_id=user_id).first()

    cells = Cell.objects.all()
    for item in cells:
        TgUserService.create_if_not_user_cell(cell=item, user=user)

    user_cells = UserCell.objects.filter(tg_user=user).order_by('cell__number')
    serializer_data = json.dumps(UserCellSerializer(user_cells, many=True).data)
    return render(request, 'advent.html', {'data': serializer_data, 'user': user, 'cells': user_cells})


def send_message(request):
    user_id = request.GET.get('user_id')
    cell_id = request.GET.get('cell_id')
    user_exists = TgUser.objects.filter(user_id=user_id).exists()
    cell_exists = Cell.objects.filter(id=cell_id).exists()
    if user_exists is False or cell_exists is False:
        return

    user_cell = UserCell.objects.filter(tg_user__user_id=user_id, cell_id=cell_id).first()
    bot = telebot.TeleBot(settings.TG_BOT_TOKEN)
    message_text = user_cell.cell.content.replace('<p>', '').replace('</p>', '').replace('<br />', '')
    message_text = html.unescape(message_text)

    try:
        photos = []
        for image in CellMessageImage.objects.filter(message_id=cell_id):
            photos.append(open(image.image.path, 'rb'))

        medias = []
        for photo_data in photos:
            if len(medias) == 0:
                medias.append(InputMediaPhoto(photo_data, caption=message_text, parse_mode='HTML'))
            else:
                medias.append(InputMediaPhoto(photo_data))

        bot.send_media_group(user_id, medias)

        if user_cell.cell.additional_info is not None and user_cell.cell.additional_info != "":
            message_text = user_cell.cell.additional_info.replace('<p>', '').replace('</p>', '').replace('<br />', '')
            message_text = html.unescape(message_text)
            bot.send_message(user_id, message_text, parse_mode='HTML')

        for photo_data in photos:
            photo_data.close()

    except Exception as e:
        print(f"{user_id}")
        print(e)

    user_cell.is_opened = True
    user_cell.save()
    return JsonResponse(data={})


def split_text(text, max_length):
    return textwrap.wrap(text, max_length)
