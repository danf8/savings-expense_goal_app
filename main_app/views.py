from django.shortcuts import render, redirect
from .models import Savings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def savings(request):
    savings = Savings.objects.filter(user=request.user)
    return render(request, 'savings/index.html', {'savings': savings})

@login_required
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

class SavingsCreate(LoginRequiredMixin, CreateView):
    model = Savings
    fields = ('save_goal', 'current_savings', 'income')
    template_name = 'savings/saving_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SavingsUpdate(LoginRequiredMixin, UpdateView):
    model = Savings
    fields = 'income',
    template_name = 'savings/saving_form.html'


class SavingsDelete(LoginRequiredMixin, DeleteView):
    model = Savings
    success_url = '/savings/'
    template_name = 'savings/delete.html'
