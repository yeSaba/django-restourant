# Generated by Django 5.1.6 on 2025-03-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_foodtype_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
