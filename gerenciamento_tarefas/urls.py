from django.contrib import admin
from django.urls import path, include
from tarefas.views import pagina_inicial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('tarefas/', include('tarefas.urls')),
    path('', pagina_inicial, name='pagina_inicial'),  # Página inicial personalizada
]
