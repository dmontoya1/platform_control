from django.urls import path

from platform_control.customers.api.views import CustomerCreate, CustomerListView


app_name = "customers"
urlpatterns = [
    # Accounts URLs
    path("", CustomerListView.as_view(), name="customer_list"),
    path("create/", CustomerCreate.as_view(), name="customer_create"),
]
