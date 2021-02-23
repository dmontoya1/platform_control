from django.urls import path

from platform_control.platforms.api.views.platform import PlatformListAPIView, PlatformCreate
from platform_control.platforms.api.views.account import AccountListView, AccountCreate
from platform_control.platforms.api.views.screen import ScreenListView


app_name = "platforms"
urlpatterns = [
    # Accounts URLs
    path("accounts/", AccountListView.as_view(), name="account_list"),
    path("account/create/", AccountCreate.as_view(), name="account_create"),

    # Platforms URLs
    path("", PlatformListAPIView.as_view(), name="platform_list"),
    path("create/", PlatformCreate.as_view(), name="platform_create"),

    # Screens URLs
    path("screens/", ScreenListView.as_view(), name="screen_list"),
]
