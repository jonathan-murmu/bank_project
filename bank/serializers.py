from rest_framework import serializers

from bank.models import Branches, Banks


class BranchSerializer(serializers.ModelSerializer):
    bank = serializers.CharField(source='bank.name')

    class Meta:
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city',
                  'district', 'state')


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'