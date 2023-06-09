# Generated by Django 4.1.7 on 2023-04-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_expenses_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expense_type',
            field=models.CharField(choices=[('R', 'Restaurant'), ('B', 'Bills & Utilities'), ('T', 'Transportation'), ('E', 'Entertainment'), ('D', 'Education'), ('V', 'Travel'), ('G', 'Groceries'), ('A', 'Gas'), ('H', 'Health & Wellness'), ('S', 'Shopping'), ('O', 'Other')], default='R', max_length=2),
        ),
    ]
