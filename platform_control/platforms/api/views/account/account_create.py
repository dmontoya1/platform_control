from rest_framework import generics

from ...serializers.account_serializer import AccountCreateSerializer


class AccountCreate(generics.CreateAPIView):
    """
    """

    serializer_class = AccountCreateSerializer
