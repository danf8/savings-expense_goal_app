from django.shortcuts import render, redirect
from .models import Savings, Expenses, AddSavings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from .forms import ExpenseForm
from django.http import JsonResponse
import requests
import environ

environ.Env.read_env()
env = environ.Env()
api_key = env.str('API_KEY', '')

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
    add_savings = AddSavings.objects.filter(user=request.user)
    expenses = Expenses.objects.filter(user=request.user)
    saving = Savings.objects.get(id=saving_id)
    total_expenses = expenses.aggregate(Sum('expense_amt'))['expense_amt__sum']
    total_added_savings = add_savings.aggregate(Sum('additional_savings'))['additional_savings__sum']
    time_in = ''
    if total_added_savings is not None and total_added_savings > 0:
        total_savings = saving.current_savings + total_added_savings 
    else:
        total_savings = saving.current_savings
    if total_expenses is not None:
            income_after_expenses = saving.monthly_income - total_expenses
            if income_after_expenses > 0:
                time_till_goal = round(((saving.save_goal / (income_after_expenses + saving.current_savings)) / 12), 2)
                time_in = 'Years'
            else: 
                time_till_goal = 'You are spending more than income currently'
                time_in = ''
    else:
        income_after_expenses = saving.monthly_income
        time_till_goal = round(((saving.save_goal / (income_after_expenses + saving.current_savings)) / 12), 2)
    expense_type_totals = expenses.values('expense_type').annotate(total=Sum('expense_amt'))
    for expense_type in expense_type_totals:
        if total_expenses is not None:
            expense_type['percentage'] = round((expense_type['total'] / total_expenses) * 100, 2)
        else:
            expense_type['percentage'] = 0
    labels = []
    data = []
    queryset = expenses
    for val in queryset:
        labels.append(val.expense_type)
        data.append(val.expense_amt)
    return render(request, 'savings/detail.html', {'saving': saving, 
                                                   'expenses': expenses, 
                                                   'total_expenses': total_expenses, 
                                                   'income_after_expenses': income_after_expenses, 
                                                   'time_till_goal': time_till_goal, 
                                                   'expense_type_totals': expense_type_totals, 
                                                   'add_savings': add_savings, 
                                                   'total_added_savings': total_added_savings, 
                                                   'total_savings': total_savings, 'labels': labels, 'data': data, 'time_in': time_in, })

@login_required
def expenses(request):
    expenses = Expenses.objects.filter(user=request.user)
    return render(request, 'expense/index.html', {'expenses': expenses})

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

@login_required
def get_financial_edu_articles(request):
    endpoint = 'https://newsapi.org/v2/everything'
    # if query is empty defaults to financial education
    query = request.GET.get('query', 'financial education')
    response = requests.get(endpoint, params={'q': query, 'apiKey': api_key})

    if response.status_code == 200:
        articles = response.json()['articles']
        # extract relevant information from the articles
        extracted_articles = [{'title': article['title'], 'description': article['description'], 'url': article['url']} for article in articles]
        # return the extracted articles as JSON response
        context = {'articles': extracted_articles}
        return render(request, 'articles.html', context)
    else:
        return render(request, 'home.html')


class SavingsCreate(LoginRequiredMixin, CreateView):
    model = Savings
    fields = ('save_goal', 'current_savings', 'monthly_income')
    template_name = 'savings/saving_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SavingsUpdate(LoginRequiredMixin, UpdateView):
    model = Savings
    fields = 'monthly_income',
    template_name = 'savings/saving_form.html'


class SavingsDelete(LoginRequiredMixin, DeleteView):
    model = Savings
    success_url = '/savings/'
    template_name = 'savings/delete.html'


class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'expense/create_expense.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpenseDetails(LoginRequiredMixin, DetailView):
    model = Expenses
    template_name = 'expense/details.html'

class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expenses
    success_url = '/expenses/'
    template_name = 'expense/delete.html'

class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expenses
    fields = ('expense_amt', 'expense_type', 'date')
    template_name = 'expense/create_expense.html'

class AdditionalSavings(LoginRequiredMixin, CreateView):
    model = AddSavings
    fields = 'additional_savings',
    template_name = 'savings/add_savings.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    

    