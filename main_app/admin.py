from django.contrib import admin

# Register your models here.
from .models import Savings, Expenses, AddSavings

admin.site.register([Savings, Expenses, AddSavings])
