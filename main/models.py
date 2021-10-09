from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_title = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        verbose_name = "Категория объявления"
        verbose_name_plural = "Категории объявлений"

    def __str__(self):
        return f"{self.category_title}"


class BaseUser(models.Model):
    user = models.OneToOneField(User, related_name="base_user", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Стандартный пользователь"
        verbose_name_plural = "Стандартные пользователи"

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


# data
class DataUnit(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    title_image = models.ImageField(verbose_name='Заглавное изображение', blank=True, upload_to='offers_title_image')
    creator = models.ForeignKey(BaseUser, related_name='creator', verbose_name='Владелец', db_index=True, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.JSONField(verbose_name="Список тегов через пробел", db_index=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    images = models.JSONField(verbose_name='Изображения', blank=True, null=True)
    document1 = models.FileField(verbose_name='Файл 1', upload_to='addition_files', blank=True)
    document2 = models.FileField(verbose_name='Файл 2', upload_to='addition_files', blank=True)
    document3 = models.FileField(verbose_name='Файл 3', upload_to='addition_files', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    customers = models.ManyToManyField(BaseUser, related_name='customer', verbose_name='Покупатели', blank=True)
    archivated = models.BooleanField(verbose_name='В архиве')

    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"

    def __str__(self):
        return f"{self.title}"