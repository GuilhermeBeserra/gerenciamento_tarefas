from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('cadastro/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path('gerenciar/', views.gerenciar_tarefas, name='gerenciar_tarefas'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),

]
