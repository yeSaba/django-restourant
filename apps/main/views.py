from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import *
from .models import *
from apps.menu.models import Chef, FoodType, Food

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chefs = Chef.objects.all()
        context['chefs'] = chefs
        foods = Food.objects.all()
        context['foods'] = foods
        book = Booking.objects.all()
        context['booking'] = book
        return  context

class ContactUs(CreateView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'

# class Subscribtion(CreateView):
#     template_name = 'base.html'
#     form_class = NewsLetterForm
#     success_url = '/'

def index(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = NewsLetterForm()
    context = {
        'form': form,
    }
    return render(request, 'base.html', context)

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ServiceView(TemplateView):
    template_name = 'pages/service.html'

class BookingView(CreateView):
    model = Booking
    template_name = 'pages/booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('home')