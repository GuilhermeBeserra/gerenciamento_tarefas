from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from usuarios.models import Usuario

def editar_tarefa(request, tarefa_id):
    # Obtém a tarefa pelo ID
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    usuarios = Usuario.objects.all()  # Lista todos os usuários

    if request.method == 'POST':
        # Recupera os dados do formulário
        usuario_id = request.POST.get('usuario')
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        prioridade = request.POST.get('prioridade')
        status = request.POST.get('status')

        # Verifica se todos os campos obrigatórios foram preenchidos
        if usuario_id and descricao and setor and prioridade:
            usuario = Usuario.objects.get(id=usuario_id)

            # Atualiza os campos da tarefa
            tarefa.usuario = usuario
            tarefa.descricao = descricao
            tarefa.setor = setor
            tarefa.prioridade = prioridade
            tarefa.status = status
            tarefa.save()

            # Redireciona para a página de gerenciamento após salvar
            return redirect('tarefas:gerenciar_tarefas')

    # Exibe o formulário de edição com os dados atuais da tarefa
    return render(request, 'tarefas/editar.html', {
        'tarefa': tarefa,
        'usuarios': usuarios,
    })

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def gerenciar_tarefas(request):
    # Organiza as tarefas por status
    tarefas = {
        'a_fazer': Tarefa.objects.filter(status='a_fazer'),
        'fazendo': Tarefa.objects.filter(status='fazendo'),
        'pronto': Tarefa.objects.filter(status='pronto'),
    }
    return render(request, 'tarefas/gerenciar.html', {'tarefas': tarefas})

def cadastrar_tarefa(request):
    usuarios = Usuario.objects.all()  # Obtém todos os usuários para o formulário

    if request.method == 'POST':
        # Recupera os dados do formulário
        usuario_id = request.POST.get('usuario')
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        prioridade = request.POST.get('prioridade')

        # Verifica se todos os campos obrigatórios foram preenchidos
        if usuario_id and descricao and setor and prioridade:
            usuario = Usuario.objects.get(id=usuario_id)

            # Cria a nova tarefa
            Tarefa.objects.create(usuario=usuario, descricao=descricao, setor=setor, prioridade=prioridade)
            return render(request, 'tarefas/cadastro.html', {
                'mensagem': 'Tarefa cadastrada com sucesso!',
                'usuarios': usuarios,
            })

        # Caso falte algum campo
        return render(request, 'tarefas/cadastro.html', {
            'erro': 'Preencha todos os campos!',
            'usuarios': usuarios,
        })

    return render(request, 'tarefas/cadastro.html', {'usuarios': usuarios})
