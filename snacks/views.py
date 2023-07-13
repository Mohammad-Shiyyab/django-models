from django.shortcuts import render
from django.views.generic import ListView,DetailView ,TemplateView
from .models import Snack

# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = "data"

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'    
    model = Snack
    
class HomeView(TemplateView):
    template_name='home.html'
    model=Snack