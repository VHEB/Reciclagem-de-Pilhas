from django.shortcuts import render, redirect
from .forms import UsuarioForm, PontoColetaForm, ContatoForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

# View para cadastro de usuário
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        confirmar_senha = request.POST.get('confirmar-senha')
        
        if form.is_valid():
            if form.cleaned_data['senha'] != confirmar_senha:
                return render(request, 'cadastroUsuario.html', {'form': form, 'erro_confirmacao': 'As senhas não coincidem.'})
            form.save()
            return redirect('sucesso')
    else:
        form = UsuarioForm()
    return render(request, 'cadastroUsuario.html', {'form': form})

# View para cadastro de ponto de coleta
def cadastrar_ponto_coleta(request):
    if request.method == 'POST':
        form = PontoColetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = PontoColetaForm()
    return render(request, 'cadastroPontoDeColeta.html', {'form': form})

# View para envio de email de contato
def enviar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            
            send_mail(
                f'Contato de {nome}',
                mensagem,
                email,
                [settings.EMAIL_HOST_USER],  # Email destinatário
            )
            return redirect('sucesso')
    else:
        form = ContatoForm()
    return render(request, 'sobre.html', {'form': form})
