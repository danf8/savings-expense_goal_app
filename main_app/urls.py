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
]