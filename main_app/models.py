from django.db import models
from django.urls import reverse

# Create your models here.

class Savings(models.Model):
    save_goal = models.IntegerField(default=0)
    current_savings = models.IntegerField(default=0)
    income = models.IntegerField(default=0)

    def __str__(self):
        return str(self.save_goal)

    