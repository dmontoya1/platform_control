from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...serializers.screen_serializer import ScreenSerializer
from ....models.screen import Screen


class ScreenDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    """

    permission_classes = [IsAuthenticated, ]
    serializer_class = ScreenSerializer
    queryset = Screen.objects.all()
