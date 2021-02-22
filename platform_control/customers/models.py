from django.db import models


class Customer(models.Model):
    name = models.CharField('Nombre', max_length=255)

    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return self.name
