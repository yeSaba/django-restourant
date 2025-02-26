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