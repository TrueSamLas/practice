from django.db import models


class Position(models.Model):
    name = models.CharField('Название', max_length=30)
    type = models.CharField('Тип', max_length=30)
    gramm = models.CharField('Литры', max_length=10)
    sostav = models.TextField('Описание')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Позиция"
        verbose_name_plural="Позиции товаров"
