from django.contrib import admin

from .models import Account, Platform, Screen


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    '''Admin View for Account'''

    list_display = ('user', 'platform', 'email', 'password', 'buy_date',
                    'renoval_date', 'screen_number', 'available_screen_number', )
    list_filter = ('email', 'platform__name', 'available_screen_number')
    search_fields = ('buy_date', 'platform__name',)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    '''Admin View for Platform'''

    list_display = ('name', 'price', )
    search_fields = ('name', 'price')


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    '''Admin View for Screen'''

    list_display = ('account', 'customer', 'buy_date', 'renoval_date', 'pin', )
    list_filter = ('customer', 'buy_date', 'renoval_date', )
    search_fields = ('account__email', 'customer__name', 'account__platform__name')
