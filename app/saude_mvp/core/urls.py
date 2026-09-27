from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/nova/', views.criar_consulta, name='criar_consulta'),
    path('consultas/editar/<int:id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/deletar/<int:id>/', views.deletar_consulta, name='deletar_consulta'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastros/', views.cadastros, name='cadastros'),

    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/novo/', views.criar_paciente, name='criar_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/excluir/<int:id>/', views.excluir_paciente, name='excluir_paciente'),

    path('profissionais/', views.listar_profissionais, name='listar_profissionais'),
    path('profissionais/novo/', views.criar_profissional, name='criar_profissional'),
    path('profissionais/editar/<int:id>/', views.editar_profissional, name='editar_profissional'),
    path('profissionais/excluir/<int:id>/', views.excluir_profissional, name='excluir_profissional'),

    path('unidades/', views.listar_unidades, name='listar_unidades'),
    path('unidades/novo/', views.criar_unidade, name='criar_unidade'),
    path('unidades/editar/<int:id>/', views.editar_unidade, name='editar_unidade'),
    path('unidades/excluir/<int:id>/', views.excluir_unidade, name='excluir_unidade'),

    path('especialidades/', views.listar_especialidades, name='listar_especialidades'),
    path('especialidades/nova/', views.criar_especialidade, name='criar_especialidade'),
    path('especialidades/editar/<int:id>/', views.editar_especialidade, name='editar_especialidade'),
    path('especialidades/excluir/<int:id>/', views.excluir_especialidade, name='excluir_especialidade'),

    path('medicamentos/', views.listar_medicamentos, name='listar_medicamentos'),
    path('medicamentos/novo/', views.criar_medicamento, name='criar_medicamento'),
    path('medicamentos/editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/excluir/<int:id>/', views.excluir_medicamento, name='excluir_medicamento'),

    path('consultas/relatorio/', views.relatorio_consultas, name='relatorio_consultas'),
    path('contato/', views.contato, name='contato'),

    path('solicitacoes/', views.listar_solicitacoes_med, name='listar_solicitacoes_med'),
    path('solicitacoes/nova/', views.criar_solicitacao_med, name='criar_solicitacao_med'),
    path('solicitacoes/itens/<int:id>/', views.adicionar_itens, name='adicionar_itens'),
    path('solicitacoes/editar/<int:id>/', views.editar_solicitacao_med, name='editar_solicitacao_med'),
    path('solicitacoes/excluir/<int:id>/', views.excluir_solicitacao_med, name='excluir_solicitacao_med'),

]