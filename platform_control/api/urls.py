from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('api-key/', views.ApiKeyDetailView.as_view(), name='api-key'),
    # path('appointments/', include('clinket.appointments.urls', namespace="appointments")),
    # path('companies/', include('clinket.companies.urls', namespace='companies')),
    # path('customers/', include('clinket.customers.urls', namespace='customers')),
    # path('global_config/', include('clinket.global_config.urls', namespace="global_config")),
    # path('notifications/', include('clinket.notifications.urls', namespace="notifications")),
    # path('payments/', include('clinket.payments.urls')),
    # path('reports/', include('clinket.reports.urls')),
    # path('users/', include('clinket.users.urls', namespace='users')),
]
