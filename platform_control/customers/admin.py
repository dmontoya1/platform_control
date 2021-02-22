from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''Admin View for Customer'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
