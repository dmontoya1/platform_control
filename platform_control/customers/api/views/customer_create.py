from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from platform_control.api.helpers import get_api_user
from ..serializers.customer_serializer import CustomerSerializer


class CustomerCreate(generics.CreateAPIView):
    """
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        user = get_api_user(self.request)
        serializer.save(user=user)
