from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('contact_us/', ContactUs.as_view(), name = 'contact_us'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('service/', ServiceView.as_view(), name = 'service'),
    path('booking/', BookingView.as_view(), name = 'booking'),
]