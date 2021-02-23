from rest_framework import generics

from ...serializers.account_serializer import AccountSerializer
from ....models import Account


class AccountListView(generics.ListAPIView):
    """
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
