from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, PontoColetaForm, ContatoForm
from django.core.mail import send_mail
from django.conf import settings
from .models import PontoColeta, Usuario
from django.http import JsonResponse


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
    usuario_logado = request.session.get('usuario_id') is not None

    if request.method == 'POST':
        if not usuario_logado:
            return redirect('login')
        
        form = PontoColetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = PontoColetaForm()

    return render(request, 'cadastroPontoDeColeta.html', {'form': form, 'usuario_logado': usuario_logado})

def listar_pontos_coleta(request):
    pontos = PontoColeta.objects.all().values("nome_empresa", "telefone", "rua", "bairro", "numero", "cep")
    return JsonResponse(list(pontos), safe=False)

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

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = Usuario.objects.filter(email=email, senha=senha).first()
        
        if usuario:
            request.session['usuario_id'] = usuario.id
            return redirect('perfil')
        else:
            return render(request, 'login.html', {'erro': 'E-mail ou senha inválidos.'})
    return render(request, 'login.html')

def perfil(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'perfil.html', {'usuario': usuario})

def logout_view(request):
    request.session.flush()  # Remove todos os dados da sessão
    return redirect('login')

def editar_perfil(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    usuario = Usuario.objects.get(id=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        confirmar_senha = request.POST.get('confirmar-senha')

        if form.is_valid():
            if form.cleaned_data['senha']:
                if form.cleaned_data['senha'] != confirmar_senha:
                    return render(request, 'editarPerfil.html', {'form': form, 'erro_confirmacao': 'As senhas não coincidem.'})
            
            form.save()
            return redirect('perfil')

    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'editarPerfil.html', {'form': form})
