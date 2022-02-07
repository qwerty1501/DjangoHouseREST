# Generated by Django 4.0.1 on 2022-01-28 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='Регистрационный номер дома')),
                ('area', models.CharField(max_length=5, verbose_name='Площадь')),
                ('types', models.CharField(choices=[(1, 'Мансардный'), (2, 'Частный'), (3, 'Балконские'), (4, 'Элитки'), (5, 'Таунхаусы'), (6, 'Пентхаусы')], max_length=50, verbose_name='Тип дома')),
                ('builder', models.CharField(max_length=60, verbose_name='Подрядчик')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]