from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('api-key/', views.ApiKeyDetailView.as_view(), name='api_key'),
    path('platform/', include('platform_control.platforms.urls', namespace="platforms")),
    path('customers/', include('platform_control.customers.urls', namespace='customers')),
    # path('users/', include('platform_control.users.urls', namespace='users')),
    path('', include(('platform_control.users.urls', 'platform_control.users'), namespace='users')),
]
