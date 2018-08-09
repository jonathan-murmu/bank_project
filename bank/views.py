from rest_framework import generics

from bank import filters
from bank.models import Branches, Banks
from bank.serializers import BranchSerializer, BankSerializer


class BranchView(generics.ListAPIView):
    """Endpoint to list the branches."""
    serializer_class = BranchSerializer
    queryset = Branches.objects.all()
    filter_backends = (filters.BankFilters,)


class BankView(generics.ListAPIView):
    """Enpoint to list the banks"""
    serializer_class =  BankSerializer
    queryset = Banks.objects.all()