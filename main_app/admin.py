from django.contrib import admin

# Register your models here.
from .models import Savings, Expenses

admin.site.register([Savings, Expenses])
