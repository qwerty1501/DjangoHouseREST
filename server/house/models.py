from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class House(models.Model):
    reg_number = models.CharField(
        'Регистрационный номер дома',
        db_index=True,
        unique=True,
        max_length=10
    )
    area = models.CharField(
        'Площадь',
        max_length=5
    )
    HOUSE_TYPE = (
        (1, 'Мансардный'),
        (2, 'Частный'),
        (3, 'Балконские'),
        (4, 'Элитки'),
        (5, 'Таунхаусы'),
        (6, 'Пентхаусы'),
    )
    types = models.CharField(
        'Тип дома',
        choices=HOUSE_TYPE,
        max_length=50
    )
    builder = models.CharField(
        'Подрядчик',
        max_length=60
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT
    )