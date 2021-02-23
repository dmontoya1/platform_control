from rest_framework import generics

from ...serializers.platform_serializer import PlatformSerializer


class PlatformCreate(generics.CreateAPIView):
    """
    """

    serializer_class = PlatformSerializer
