from django.shortcuts import render
from cliente.models import Cliente


def index_admin(request):
    actividades = [
        {
            "id": cliente.pk,
            "usuario": cliente.nombre,
            "accion": "Registro de cliente",
            "fecha": cliente.fecha_registro,
        }
        for cliente in Cliente.objects.order_by("-fecha_registro")[:10]
    ]
    return render(
        request,
        "administrador/index.html",
        {
            "actividades": actividades,
            "dias_semana": ["L", "M", "X", "J", "V", "S", "D"],
        },
    )