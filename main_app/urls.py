from django.urls import path
from . import views

urlpatterns= [
    path('', views.home),
    path('accounts/signup', views.signup, name='signup'),
    path('about/', views.about),
    path('savings/', views.savings, name='savings_index'),
    path('savings/<int:saving_id>/', views.saving_details, name='saving_details'),
    path('savings/create/', views.SavingsCreate.as_view(), name='saving_create'),
    path('savings/<int:pk>/update/', views.SavingsUpdate.as_view(), name='update_savings'),
    path('savings/<int:pk>/delete/',views.SavingsDelete.as_view(), name='delete_savings'),
    path('expenses/', views.expenses, name='expense_view'),
    path('expenses/create/', views.ExpenseCreate.as_view(), name='create_expense'),
    path('expenses/<int:pk>/details/', views.ExpenseDetails.as_view(), name='expense_details'),
    path('expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='delete_expense'),
    path('expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='update_expense'),
    path('savings/add_savings/', views.AdditionalSavings.as_view(), name='additional_savings'),
]