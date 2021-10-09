# Generated by Django 3.2.8 on 2021-10-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseuser',
            options={'verbose_name': 'Стандартный пользователь', 'verbose_name_plural': 'Стандартные пользователи'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория объявления', 'verbose_name_plural': 'Категории объявлений'},
        ),
        migrations.AlterModelOptions(
            name='dataunit',
            options={'verbose_name': 'объявление', 'verbose_name_plural': 'объявления'},
        ),
        migrations.AlterField(
            model_name='dataunit',
            name='images',
            field=models.JSONField(blank=True, null=True, verbose_name='Изображения'),
        ),
    ]
