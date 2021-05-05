from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...serializers.screen_serializer import ScreenCreateSerializer


class ScreenCreate(generics.CreateAPIView):
    """
    """

    permission_classes = [IsAuthenticated, ]

    serializer_class = ScreenCreateSerializer
