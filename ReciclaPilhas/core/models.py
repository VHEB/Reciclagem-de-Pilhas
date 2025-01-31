from django.db import models

# Modelo de cadastro de usuário
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)  # Armazenar com hash no futuro

    def __str__(self):
        return self.nome

# Modelo de cadastro de ponto de coleta
class PontoColeta(models.Model):
    nome_empresa = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    rua = models.CharField(max_length=150, default='Rua Principal') 
    cep = models.CharField(max_length=9, default='00000-000')     
    bairro = models.CharField(max_length=100, default='Centro')  
    numero = models.CharField(max_length=10, default='S/N')

    def __str__(self):
        return self.nome_empresa

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return f"Mensagem de {self.nome}"
