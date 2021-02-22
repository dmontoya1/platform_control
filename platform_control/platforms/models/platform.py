from django.db import models


class Platform(models.Model):
    """Model definition for Platform."""

    name = models.CharField('Nombre', max_length=50)
    price = models.IntegerField('Precio')

    class Meta:
        """Meta definition for Platform."""

        verbose_name = 'Platforma'
        verbose_name_plural = 'Platformas'

    def __str__(self):
        """Unicode representation of Platform."""
        return self.name
