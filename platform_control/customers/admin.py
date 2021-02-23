from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''Admin View for Customer'''

    list_display = ('name', 'user')
    list_filter = ('name', 'user')
    search_fields = ('name', 'user__email')
