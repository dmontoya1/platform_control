from rest_framework import serializers

from platform_control.users.api.serializers import UserSerializer

from ...models import Account
from .platform_serializer import PlatformSerializer


class AccountSerializer(serializers.ModelSerializer):
    """
    """

    user = UserSerializer(many=False)
    platform = PlatformSerializer(many=False)

    buy_date = serializers.DateField(format='%d-%m-%Y')
    renoval_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Account
        fields = ('id', 'user', 'platform', 'email', 'password', 'buy_date',
                  'renoval_date', 'screen_number', 'available_screen_number', )


class AccountCreateSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Account
        fields = ('id', 'user', 'platform', 'email', 'password', 'buy_date',
                  'renoval_date', 'screen_number', 'available_screen_number', )
