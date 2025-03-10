from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import *
from .models import *


class HomeView(TemplateView):
    template_name = 'pages/index.html'

class ContactUs(CreateView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'

class Subscribtion(CreateView):
    template_name = 'base.html'
    form_class = NewsLetterForm
    success_url = '/'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ServiceView(TemplateView):
    template_name = 'pages/service.html'

class BookingView(CreateView):
    template_name = 'pages/booking.html'
    form_class = BookingForm
    success_url = '/'




    # def form_valid(self, form):
    #     messages.success(self.request, "Your booking has been successfully created!")
    #     return super().form_valid(form)