from django.urls import path, include 
from contas import views

urlpatterns = [
    path('desconectado-inatividade/',  views.timeout_view, name='timeout'), 
    path('login/', views.login_view, name='login'), # Adicionar rota entrar
    path('criar-conta/', views.register_view, name='register'), 
    path('logout/', views.logout_view, name='logout'),
    path("", include("django.contrib.auth.urls")),  # Django auth
    path('atualizar-usuario/', views.atualizar_meu_usuario, name='atualizar_meu_usuario'),
    path('atualizar-usuario/<slug:username>/',  views.atualizar_usuario, name='atualizar_usuario'),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('adicionar-usuario/',  views.adicionar_usuario, name='adicionar_usuario'),
]