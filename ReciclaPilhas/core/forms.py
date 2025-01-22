# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario, PontoColeta, Contato

# Validadores adicionais
def validar_email_unico(email):
    if Usuario.objects.filter(email=email).exists():
        raise ValidationError('Este email já está cadastrado.')

def validar_senha(senha):
    if len(senha) < 8:
        raise ValidationError('A senha deve ter pelo menos 8 caracteres.')
    

# Formulário de cadastro de usuário
class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)  # Oculta a senha

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']

    def clean_email(self):
        email = self.cleaned_data['email']
        validar_email_unico(email)
        return email
# Formulário de cadastro de ponto de coleta
class PontoColetaForm(forms.ModelForm):
    class Meta:
        model = PontoColeta
        fields = ['nome_empresa', 'telefone', 'endereco', 'rua', 'cep', 'bairro', 'numero']


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

