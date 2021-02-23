# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Django
from django.contrib.auth import get_user_model

# Serializers
from .serializers import UserLoginSerializer, UserSerializer

# Models
User = get_user_model()


class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
