import datetime

from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Электронная почта', max_length=70)
    subject = models.CharField('Тема', max_length=50)
    text = models.TextField('Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'



class NewsLetter(models.Model):
    email = models.EmailField('Электронная почта', max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'



class Booking(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Почта', max_length=100, unique=True)
    time = models.DateTimeField('Дата и время')
    people = models.IntegerField('Количество людей')
    request = models.TextField('Особые предпочтения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'