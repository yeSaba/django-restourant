from django.urls import path
from .views import *

urlpatterns = [
    path('team/', ChefListView.as_view(), name = 'team'),
    path('menu/', FoodListView.as_view(), name = 'foods'),
]