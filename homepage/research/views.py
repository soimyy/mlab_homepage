from django.shortcuts import render
from .models import Research
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    model = Research
