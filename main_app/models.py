from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Savings(models.Model):
    save_goal = models.IntegerField(default=0)
    current_savings = models.IntegerField(default=0)
    monthly_income = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('saving_details', kwargs={'saving_id': self.id})

    def __str__(self):
        return str(self.save_goal)
    
class Expenses(models.Model):
    EXPENSE_TYPE = (
        ('Restaurant','Restaurant'),
        ('Bills & Utilities', 'Bills & Utilities'),
        ('Transportation','Transportation'),
        ('Entertainment','Entertainment'),
        ('Education','Education'),
        ('Travel','Travel'),
        ('Groceries','Groceries'),
        ('Gas','Gas'),
        ('Health & Wellness','Health & Wellness'),
        ('Shopping','Shopping'),
        ('Other','Other'),
        )
    expense_amt = models.IntegerField(default=0)
    expense_type = models.CharField(max_length=25, choices=EXPENSE_TYPE, default=EXPENSE_TYPE[0][0])
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('expense_details', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.expense_amt)
    
    class Meta:
        ordering = '-date',

    