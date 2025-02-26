from django.contrib import admin
from .models import ContactUs, NewsLetter
# Register your models here.

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'text',
        'created_at'
    ]
    list_filter = ['created_at']
    search_fields = ['name',
                     'email',]

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'created_at'
    ]
    list_filter = ['created_at']
    search_fields = ['email']