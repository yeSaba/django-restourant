from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class ChefListView(ListView):
    model = Chef
    template_name = 'pages/team.html'
    context_object_name = 'chefs'
    paginate_by = 4

class FoodListView(ListView):
    model = Food
    template_name = 'pages/menu.html'
    context_object_name = 'foods'