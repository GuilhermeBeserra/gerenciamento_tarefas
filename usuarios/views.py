from django.shortcuts import render, redirect
from .models import Usuario

def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        if nome and email:
            Usuario.objects.create(nome=nome, email=email)
            return render(request, 'usuarios/cadastro.html', {'mensagem': 'Usuário cadastrado com sucesso!'})
        else:
            return render(request, 'usuarios/cadastro.html', {'erro': 'Preencha todos os campos!'})

    return render(request, 'usuarios/cadastro.html')
