# Generated by Django 5.0.7 on 2024-11-19 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('setor', models.CharField(max_length=255)),
                ('prioridade', models.CharField(choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')], default='baixa', max_length=10)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('a_fazer', 'A Fazer'), ('fazendo', 'Fazendo'), ('pronto', 'Pronto')], default='a_fazer', max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
