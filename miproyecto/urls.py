from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-django/', admin.site.urls),
    path('', include('cliente.urls')),
    path('admin-panel/', include('administrador.urls')),
]