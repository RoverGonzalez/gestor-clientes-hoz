from django.db import models

# Create your models here.

class Cliente(models.Model):
    cuit = models.PositiveBigIntegerField(primary_key=True, max_length=11)
    empresa = models.CharField(max_length=20)
    empleado = models.CharField(max_length=20)
    cargo = models.CharField(max_length=30)

    def __str__(self):
        texto = "{0} - {1} ({2})"
        return texto.format(self.empresa, self.empleado, self.cargo)