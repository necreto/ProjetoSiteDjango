from django.urls import path, include 
from contas import views

urlpatterns = [
    path('desconectado-inatividade/',  views.timeout_view, name='timeout'), 
    path('login/', views.login_view, name='login'), # Adicionar rota entrar
    path('criar-conta/', views.register_view, name='register'), 
    path('logout/', views.logout_view, name='logout'),
    path("", include("django.contrib.auth.urls")),  # Django auth
]