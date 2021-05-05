from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...serializers.platform_serializer import PlatformSerializer
from ....models.platform import Platform


class PlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    """

    permission_classes = [IsAuthenticated, ]
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()
