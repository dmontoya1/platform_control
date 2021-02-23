# from django.urls import path
# from .api.views import UserViewSet
#
#
# app_name = "users"
# urlpatterns = [
#     path("login/", UserViewSet.login(), name="user_login"),
# ]

"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .api import views as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')

app_name = "users"
urlpatterns = [
    path('', include(router.urls))
]
