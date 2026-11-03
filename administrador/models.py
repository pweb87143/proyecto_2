from django.db import models

class ReporteGestion(models.Model):
    titulo = models.CharField(max_length=150)                      # 1. CharField
    descripcion = models.TextField()                                # 2. TextField
    resuelto = models.BooleanField(default=False)                   # 3. BooleanField
    fecha_creacion = models.DateTimeField(auto_now_add=True)        # 4. DateTimeField

    def __str__(self):
        return self.titulo