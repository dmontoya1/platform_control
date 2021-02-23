from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Customer(models.Model):
    name = models.CharField('Nombre', max_length=255)
    user = models.ForeignKey(
        User,
        verbose_name="Usuario al que pertenece el cliente",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return self.name
