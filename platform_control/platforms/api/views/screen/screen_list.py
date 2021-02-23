from rest_framework import generics

from ...serializers.screen_serializer import ScreenSerializer
from ....models import Screen


class ScreenListView(generics.ListAPIView):
    """
    """

    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer
