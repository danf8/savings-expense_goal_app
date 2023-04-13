from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Savings(models.Model):
    save_goal = models.IntegerField(default=0)
    current_savings = models.IntegerField(default=0)
    income = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('saving_details', kwargs={'saving_id': self.id})

    def __str__(self):
        return str(self.save_goal)
    


    