from rest_framework import serializers

from platform_control.customers.api.serializers.customer_serializer import CustomerSerializer

from ...models import Screen
from .account_serializer import AccountSerializer


class ScreenSerializer(serializers.ModelSerializer):
    """
    """

    account = AccountSerializer(many=False)
    customer = CustomerSerializer(many=False)

    buy_date = serializers.DateField(format='%d-%m-%Y')
    renoval_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Screen
        fields = ('id', 'account', 'customer', 'buy_date', 'renoval_date', 'pin', )
