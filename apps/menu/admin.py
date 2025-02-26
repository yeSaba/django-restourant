from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = [
        'avatar',
        'first_name',
        'last_name',
        'position',
        'social_media_link',
        'created_at',
    ]
    list_filter = ['created_at']
    search_fields = ['position',
                     'first_name',
                     'last_name', ]