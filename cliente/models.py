from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)                     # 1. CharField
    email = models.EmailField(unique=True)                        # 2. EmailField
    telefono = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)                    # 3. BooleanField (Campo agregado)
    fecha_registro = models.DateTimeField(auto_now_add=True)      # 4. DateTimeField

    def __str__(self):
        return self.nombre