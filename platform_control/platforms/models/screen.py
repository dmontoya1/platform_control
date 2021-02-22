from django.db import models

from platform_control.customers.models import Customer
from .account import Account


class Screen(models.Model):
    """Model definition for Screen."""

    account = models.ForeignKey(Account, verbose_name="Cuenta", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="Cliente", on_delete=models.CASCADE)
    buy_date = models.DateField("Fecha de compra", auto_now=False, auto_now_add=False)
    renoval_date = models.DateField("Fecha de renovación", auto_now=False, auto_now_add=False)
    pin = models.CharField("PIN", max_length=4)

    class Meta:
        """Meta definition for Screen."""

        verbose_name = 'Pantalla'
        verbose_name_plural = 'Pantallas'

    def __str__(self):
        """Unicode representation of Screen."""
        return "Pantalla de {} de la cuenta {}".format(self.customer, self.account)
    
    
