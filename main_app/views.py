from django.shortcuts import render
from .models import Savings
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def savings(request):
    savings = Savings.objects.all()
    return render(request, 'savings/index.html', {'savings': savings})