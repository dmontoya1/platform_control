from rest_framework import permissions
from .models import APIKey


class HasAPIAccess(permissions.BasePermission):
    """
    Clase para dar permisos de a las API
    """
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        if request.META.get('HTTP_X_API_KEY', None):
            api_key = request.META['HTTP_X_API_KEY']
        else:
            api_key = request.META.get('HTTP_API_KEY', '')
        return APIKey.objects.filter(key=api_key).exists()
