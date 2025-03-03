from django.db import models

# Create your models here.
class Chef(models.Model):
    avatar = models.ImageField('Фото', upload_to='media/',blank=True,null=True)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    position = models.CharField('Позиция', max_length=100)
    social_media_link = models.URLField('Ссылка на СС', max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

    class Meta:
        verbose_name = 'Шеф повар'
        verbose_name_plural = 'Шеф повара'



class FoodType(models.Model):
    name = models.CharField('Тип', max_length=50)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'Тип блюда'
        verbose_name_plural = 'Типы блюд'

class Food(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    ingredients = models.TextField()
    calories = models.IntegerField()
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бладо'
        verbose_name_plural = 'Блюда'