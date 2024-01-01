from django.db import models
from djrichtextfield.models import RichTextField


class Cell(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер ячейки')
    description = models.CharField(verbose_name='Краткое описание', max_length=250)
    webapp_image = models.ImageField(upload_to='upload/', verbose_name='Аватар')
    name = models.CharField(verbose_name="ФИО", max_length=126, default="")
    content = RichTextField(max_length=1010, verbose_name="Текст под фото")
    additional_info = RichTextField(max_length=4000, verbose_name="Текст доп сообщении", null=True, blank=True)
    open_date = models.DateField(verbose_name="Когда будет доступен")

    class Meta:
        verbose_name = 'Ячейка'
        verbose_name_plural = 'Ячейки'

    def __str__(self):
        return f"номер: {self.number} дата: {self.open_date.day}.{self.open_date.month}"
