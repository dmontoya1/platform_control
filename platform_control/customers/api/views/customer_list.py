from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from platform_control.api.helpers import get_api_user

from ..serializers.customer_serializer import CustomerSerializer
from ...models import Customer


class CustomerListView(generics.ListAPIView):
    """
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = get_api_user(self.request)
        return Customer.objects.filter(user=user)
