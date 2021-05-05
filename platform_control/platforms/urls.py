from django.urls import path

from platform_control.platforms.api.views.platform import PlatformListAPIView, PlatformCreate, PlatformDetail
from platform_control.platforms.api.views.account import AccountListView, AccountCreate
from platform_control.platforms.api.views.screen import ScreenListView, ScreenCreate, ScreenDetail


app_name = "platforms"
urlpatterns = [
    # Accounts URLs
    path("accounts/", AccountListView.as_view(), name="account_list"),
    path("account/create/", AccountCreate.as_view(), name="account_create"),

    # Platforms URLs
    path("", PlatformListAPIView.as_view(), name="platform_list"),
    path("create/", PlatformCreate.as_view(), name="platform_create"),
    path("<int:pk>/", PlatformDetail.as_view(), name="platform_detail"),

    # Screens URLs
    path("screen/create/", ScreenCreate.as_view(), name="screen_create"),
    path("screens/", ScreenListView.as_view(), name="screen_list"),
    path("screen/<int:pk>/", ScreenDetail.as_view(), name="screen_detail")
]
