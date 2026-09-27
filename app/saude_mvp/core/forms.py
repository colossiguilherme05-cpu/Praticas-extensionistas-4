from django import forms
from django.contrib.auth.models import User
from .models import Consulta, Especialidade, ItemSolicitacao, Medicamento, Paciente, ProfissionalSaude, SolicitacaoMedicamento, UnidadeSaude

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class CadastroUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Senha"
        )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ['data_con', 'hora_con', 'id_pac', 'id_prof', 'id_uni']

        labels = {
            'data_con': 'Data da consulta',
            'hora_con': 'Hora da consulta',
            'status_con': 'Status da consulta',
            'id_pac': 'Paciente',
            'id_prof': 'Profissional de saúde',
            'id_uni': 'Unidade de saúde',
        }
        widgets = {
            'data_con': forms.DateInput(attrs={'type': 'date'}),
            'hora_con': forms.TimeInput(attrs={'type': 'time'}),
        }

class EditarConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = [
            'data_con',
            'hora_con',
            'status_con',
            'id_pac',
            'id_prof',
            'id_uni',
            'observacoes'
        ]

        labels = {
            'data_con': 'Data da consulta',
            'hora_con': 'Hora da consulta',
            'status_con': 'Status da consulta',
            'id_pac': 'Paciente',
            'id_prof': 'Profissional de saúde',
            'id_uni': 'Unidade de saúde',
        }

        widgets = {
            'data_con': forms.DateInput(attrs={'type': 'date'},format='%Y-%m-%d'),
            'hora_con': forms.TimeInput(attrs={'type': 'time'}),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

        labels = {
            'nome_pac': 'Nome do paciente',
            'cpf': 'CPF',
            'datanasc': 'Data de nascimento',
            'numtelefone': 'Telefone',
            'email': 'E-mail',
            'senha': 'Senha',
        }

        widgets = {
            'datanasc': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'

        labels = {
            'nome_prof': 'Nome do profissional',
            'crm_prof': 'CRM do profissional',
            'id_esp': 'Especialidade médica',
        }

class UnidadeForm(forms.ModelForm):
    class Meta:
        model = UnidadeSaude
        fields = '__all__'

        labels = {
            'nome_uni': 'Nome da unidade',
            'endereco_uni': 'Endereço',
        }

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = '__all__'

        labels = {
            'nome_esp': 'Nome da especialidade médica',
        }

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        
        labels = {
            'nome_med': 'Nome do medicamento',
            'descricao': 'Descrição',
            'estoque': 'Quantidade em estoque',
        }

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoMedicamento
        fields = ['id_pac']

class ItemSolicitacaoForm(forms.ModelForm):
    class Meta:
        model = ItemSolicitacao
        fields = ['id_med', 'quant_itemsolic']
