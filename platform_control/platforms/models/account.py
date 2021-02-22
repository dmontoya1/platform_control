from .platform import Platform
from platform_control.users.models import User
from django.db import models


class Account(models.Model):
    """Model definition for Account."""

    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, verbose_name="Plataforma", on_delete=models.CASCADE)
    email = models.EmailField("Correo electrónico", max_length=254)
    password = models.CharField("Contraseña", max_length=50)
    buy_date = models.DateField("Fecha de compra", auto_now=False, auto_now_add=False)
    renoval_date = models.DateField("Fecha de renovación", auto_now=False, auto_now_add=False)
    screen_number = models.IntegerField("Número de pantallas Totales", default=0)
    available_screen_number = models.IntegerField("Número de pantallas disponibles", default=0)

    class Meta:
        """Meta definition for Account."""
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'

    def __str__(self):
        """Unicode representation of Account."""
        return "Cuenta de {} con correo {}".format(self.platform, self.email)

    def get_available_screens(self):
        return self.available_screen_number
