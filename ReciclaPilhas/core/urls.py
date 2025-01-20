from django.urls import path
from django.shortcuts import render
from core import views

urlpatterns = [
    path('', views.home, name='home'),  # Adiciona a rota para a página inicial
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar_ponto/', views.cadastrar_ponto_coleta, name='cadastrar_ponto'),
    path('contato/', views.enviar_contato, name='contato'),
    path('sucesso/', lambda request: render(request, 'formularios/sucesso.html'), name='sucesso'),
]
