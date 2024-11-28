from django.db import models
from usuarios.models import Usuario

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS_CHOICES = [
        ('fazer', 'Fazer'),
        ('fazendo', 'Fazendo'),
        ('pronto', 'Pronto'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.TextField()
    setor = models.CharField(max_length=255)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='baixa')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='a_fazer')

    def __str__(self):
        return f"{self.descricao} ({self.usuario.nome})"
