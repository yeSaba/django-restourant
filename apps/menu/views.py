from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        food_types = FoodType.objects.all()
        context['food_types'] = food_types
        return context