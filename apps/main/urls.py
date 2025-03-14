from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('news_letter/', views.index, name = 'news_letter'),
    path('contact_us/', ContactUs.as_view(), name = 'contact_us'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('service/', ServiceView.as_view(), name = 'service'),
    path('booking/', BookingView.as_view(), name = 'booking'),
]