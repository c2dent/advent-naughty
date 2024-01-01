from django.db import models


class CellMessageImage(models.Model):
    message = models.ForeignKey('main.Cell', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/')

    class Meta:
        verbose_name = "карточка сообщении"
        verbose_name_plural = "карточки сообщении"
