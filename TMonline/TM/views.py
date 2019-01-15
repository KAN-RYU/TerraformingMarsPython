from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from TM.models import TM

# Create your views here.
class TmList(ListView):
    model = TM

class TmDetail(DetailView):
    model = TM

class TmGrid(TemplateView):
    template_name = "TM/tm_grid.html"
