from rest_framework import generics
from rest_framework.permissions import AllowAny

from ...serializers.platform_serializer import PlatformSerializer
from ....models import Platform


class PlatformListAPIView(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
