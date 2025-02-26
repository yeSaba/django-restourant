from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContactUsForm, NewsLetterForm
from .models import NewsLetter


class HomeView(TemplateView):
    template_name = 'pages/index.html'

class ContactUs(CreateView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'

class Subscribtion(TemplateView):
    template_name = 'base.html'
    form_class = NewsLetterForm
    success_url = '/'