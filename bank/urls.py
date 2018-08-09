from django.urls import path

from bank.views import BranchView, BankView

urlpatterns = [
    path('branches/', BranchView.as_view(), name='bank-branches'),
    path('banks/', BankView.as_view(), name='bank')
]