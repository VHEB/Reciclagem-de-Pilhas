from django import forms
from django.core.mail.message import EmailMessage
from .models import Usuario, PontoColeta, Contato

# Formulário de cadastro de usuário
class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)  # Oculta a senha

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']

# Formulário de cadastro de ponto de coleta
class PontoColetaForm(forms.ModelForm):
    class Meta:
        model = PontoColeta
        fields = ['nome_empresa', 'telefone', 'endereco']


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']