from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from main.forms import CellMessageForm, PlannedMessageForm
from main.models import TgUser, PlannedMessage
from main.models.cell import Cell
from main.models.cell_message_image import CellMessageImage
from main.models.message_image import MessageImage


@admin.register(TgUser)
class Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_id', 'id']


class ImageFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        count = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                count += 1
        if count < 1:
            raise ValidationError('Вы должны добавить хотя бы одно изображение.')


class ImageInline(admin.TabularInline):
    model = MessageImage
    formset = ImageFormSet
    extra = 1


class CellMessageImageInline(admin.TabularInline):
    model = CellMessageImage
    formset = ImageFormSet
    extra = 1


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    form = CellMessageForm
    inlines = [CellMessageImageInline]
    list_display = ['number', 'open_date']


@admin.register(PlannedMessage)
class PlannedMessageAdmin(admin.ModelAdmin):
    form = PlannedMessageForm
    inlines = [ImageInline]
    list_display = ['is_sent', 'send_time']
