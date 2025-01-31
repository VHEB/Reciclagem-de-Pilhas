from django.urls import path
from django.shortcuts import render
from core import views
from django.conf import settings
from django.conf.urls.static import static
from .views import listar_pontos_coleta


urlpatterns = [
    path('', views.home, name='home'),  # Adiciona a rota para a página inicial
    path('cadastroUsuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastroPontoDeColeta/', views.cadastrar_ponto_coleta, name='cadastrar_ponto'),
    path('sobre/', views.enviar_contato, name='sobre'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logout_view, name='logout'),
    path("pontos-coleta/", listar_pontos_coleta, name="pontos_coleta"),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('sucesso/', lambda request: render(request, 'sucesso.html'), name='sucesso'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

