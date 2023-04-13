from django.shortcuts import render, redirect
from .models import Savings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def savings(request):
    savings = Savings.objects.all()
    return render(request, 'savings/index.html', {'savings': savings})

def saving_details(request, saving_id):
    saving = Savings.objects.get(id=saving_id)
    return render(request, 'savings/detail.html', {'saving': saving})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('savings_index')
        else:
            error_message = 'OOPS, not a valid sign up - try again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error': error_message})


class SavingsCreate(CreateView):
    model = Savings
    fields = '__all__'
    template_name = 'savings/saving_form.html'

class SavingsUpdate(UpdateView):
    model = Savings
    fields = 'income',
    template_name = 'savings/saving_form.html'


class SavingsDelete(DeleteView):
    model = Savings
    success_url = '/savings/'
    template_name = 'savings/delete.html'
