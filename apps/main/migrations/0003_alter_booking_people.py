# Generated by Django 5.1.6 on 2025-03-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.IntegerField(verbose_name='Количество людей'),
        ),
    ]
