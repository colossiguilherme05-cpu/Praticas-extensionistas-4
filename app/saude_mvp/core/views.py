from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
import datetime
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from .models import Consulta, Contato, Especialidade, ItemSolicitacao, Medicamento, Paciente, ProfissionalSaude, SolicitacaoMedicamento, UnidadeSaude
from .forms import ConsultaForm, CadastroUserForm, EditarConsultaForm, EspecialidadeForm, ItemSolicitacaoForm, MedicamentoForm, PacienteForm, ProfissionalForm, SolicitacaoForm, UnidadeForm

def home_redirect(request):
    return redirect('login')

def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/listar.html', {'consultas': consultas})


def criar_consulta(request):
    form = ConsultaForm(request.POST or None)

    if form.is_valid():
        nova = form.save(commit=False)

        data = nova.data_con
        hora = nova.hora_con
        prof = nova.id_prof

        inicio = datetime.datetime.combine(data, hora)
        inicio_min = inicio - timedelta(minutes=15)
        inicio_max = inicio + timedelta(minutes=15)

        conflitos = Consulta.objects.filter(
            id_prof=prof,
            data_con=data
        )

        for c in conflitos:
            existente = datetime.datetime.combine(c.data_con, c.hora_con)

            if inicio_min <= existente <= inicio_max:
                messages.error(request, "Profissional já possui consulta neste intervalo de 15 minutos.")
                return render(request, 'consultas/form.html', {'form': form})

        nova.save()
        return redirect('listar_consultas')

    return render(request, 'consultas/form.html', {'form': form})


def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)

    form = EditarConsultaForm(request.POST or None, instance=consulta)

    if form.is_valid():
        form.save()
        return redirect('listar_consultas')

    return render(request, 'consultas/form.html', {'form': form})

def deletar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)

    if request.method == 'POST':
        consulta.delete()
        return redirect('listar_consultas')

    return render(request, 'consultas/confirmar_exclusao.html', {
        'consulta': consulta
    })

def contato(request):
    if request.method == "POST":
        Contato.objects.create(
            nome=request.POST['nome'],
            email=request.POST['email'],
            mensagem=request.POST['mensagem']
        )
    return render(request, 'contato.html')

def cadastrar_usuario(request):
    if request.method == "POST":
        form = CadastroUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = CadastroUserForm()

    return render(request, 'cadastro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def cadastros(request):
    return render(request, 'cadastros_admin.html')

def criar_paciente(request):
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cadastros')

    return render(request, 'pacientes/form.html', {'form': form})

def listar_pacientes(request):
    pacientes = Paciente.objects.all()

    return render(
        request,
        'pacientes/listar.html',
        {'pacientes': pacientes}
    )

def editar_paciente(request, id):

    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)

        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')

    else:
        form = PacienteForm(instance=paciente)

    return render(
        request,
        'pacientes/form.html',
        {
            'form': form,
            'titulo': 'Editar Paciente'
        }
    )

def excluir_paciente(request, id):

    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')

    return render(
        request,
        'pacientes/excluir.html',
        {'paciente': paciente}
    )

def listar_profissionais(request):
    profissionais = ProfissionalSaude.objects.all()

    return render(
        request,
        'profissionais/listar.html',
        {'profissionais': profissionais}
    )

def criar_profissional(request):
    form = ProfissionalForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cadastros')

    return render(request, 'profissionais/form.html', {'form': form})


def editar_profissional(request, id):

    profissional = get_object_or_404(ProfissionalSaude, id=id)

    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)

        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')

    else:
        form = ProfissionalForm(instance=profissional)

    return render(
        request,
        'profissionais/form.html',
        {
            'form': form,
            'titulo': 'Editar Profissional'
        }
    )

def excluir_profissional(request, id):

    profissional = get_object_or_404(ProfissionalSaude, id=id)

    if request.method == 'POST':
        profissional.delete()
        return redirect('listar_profissionais')

    return render(
        request,
        'profissionais/excluir.html',
        {'profissional': profissional}
    )

def listar_unidades(request):
    unidades = UnidadeSaude.objects.all()

    return render(
        request,
        'unidades/listar.html',
        {'unidades': unidades}
    )

def criar_unidade(request):
    form = UnidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cadastros')

    return render(request, 'unidades/form.html', {'form': form})

def editar_unidade(request, id):

    unidade = get_object_or_404(UnidadeSaude, id=id)

    if request.method == 'POST':
        form = UnidadeForm(request.POST, instance=unidade)

        if form.is_valid():
            form.save()
            return redirect('listar_unidades')

    else:
        form = UnidadeForm(instance=unidade)

    return render(
        request,
        'unidades/form.html',
        {
            'form': form,
            'titulo': 'Editar Unidade'
        }
    )

def excluir_unidade(request, id):

    unidade = get_object_or_404(UnidadeSaude, id=id)

    if request.method == 'POST':
        unidade.delete()
        return redirect('listar_unidades')

    return render(
        request,
        'unidades/excluir.html',
        {'unidade': unidade}
    )

def listar_especialidades(request):
    especialidades = Especialidade.objects.all()

    return render(
        request,
        'especialidades/listar.html',
        {'especialidades': especialidades}
    )

def criar_especialidade(request):
    form = EspecialidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cadastros')

    return render(request, 'especialidades/form.html', {'form': form})

def editar_especialidade(request, id):

    especialidade = get_object_or_404(Especialidade, id=id)

    if request.method == 'POST':
        form = EspecialidadeForm(request.POST, instance=especialidade)

        if form.is_valid():
            form.save()
            return redirect('listar_especialidades')

    else:
        form = EspecialidadeForm(instance=especialidade)

    return render(
        request,
        'especialidades/form.html',
        {
            'form': form,
            'titulo': 'Editar Especialidade'
        }
    )

def excluir_especialidade(request, id):

    especialidade = get_object_or_404(Especialidade, id=id)

    if request.method == 'POST':
        especialidade.delete()
        return redirect('listar_especialidades')

    return render(
        request,
        'especialidades/excluir.html',
        {'especialidade': especialidade}
    )

def listar_medicamentos(request):
    medicamentos = Medicamento.objects.all()

    return render(
        request,
        'medicamentos/listar.html',
        {'medicamentos': medicamentos}
    )

def criar_medicamento(request):
    form = MedicamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cadastros')

    return render(request, 'medicamentos/form.html', {'form': form})

def editar_medicamento(request, id):

    medicamento = get_object_or_404(Medicamento, id=id)

    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)

        if form.is_valid():
            form.save()
            return redirect('listar_medicamentos')

    else:
        form = MedicamentoForm(instance=medicamento)

    return render(
        request,
        'medicamentos/form.html',
        {
            'form': form,
            'titulo': 'Editar Medicamento'
        }
    )

def excluir_medicamento(request, id):

    medicamento = get_object_or_404(Medicamento, id=id)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('listar_medicamentos')

    return render(
        request,
        'medicamentos/excluir.html',
        {'medicamento': medicamento}
    )

def relatorio_consultas(request):

    consultas = Consulta.objects.all()

    status = request.GET.get('status')
    paciente = request.GET.get('paciente')
    profissional = request.GET.get('profissional')
    unidade = request.GET.get('unidade')
    data = request.GET.get('data')
    hora = request.GET.get('hora')

    if status and status != 'TODOS':
        consultas = consultas.filter(status_con=status)

    if paciente:
        consultas = consultas.filter(id_pac_id=paciente)

    if profissional:
        consultas = consultas.filter(id_prof_id=profissional)

    if unidade:
        consultas = consultas.filter(id_uni_id=unidade)

    if data:
        consultas = consultas.filter(data_con=data)

    if hora:
        consultas = consultas.filter(hora_con=hora)

    total = consultas.count()
    agendadas = consultas.filter(status_con='AGENDADA').count()
    realizadas = consultas.filter(status_con='REALIZADA').count()
    canceladas = consultas.filter(status_con='CANCELADA').count()

    return render(request, 'consultas/relatorio.html', {
        'consultas': consultas,
        'total': total,
        'agendadas': agendadas,
        'realizadas': realizadas,
        'canceladas': canceladas,
        'pacientes': Paciente.objects.all(),
        'profissionais': ProfissionalSaude.objects.all(),
        'unidades': UnidadeSaude.objects.all(),
    })

def contato(request):
    if request.method == 'POST':
        Contato.objects.create(
            nome=request.POST['nome'],
            email=request.POST['email'],
            mensagem=request.POST['mensagem']
        )

        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato')

    return render(request, 'contato.html')

def criar_solicitacao_med(request):

    form = SolicitacaoForm(request.POST or None)

    if form.is_valid():
        solicitacao = form.save()

        return redirect('adicionar_itens', solicitacao.id)

    return render(request, 'solicitacao_medicamento/form.html', {
        'form': form
    })

def adicionar_itens(request, id):

    solicitacao = get_object_or_404(SolicitacaoMedicamento, id=id)

    form = ItemSolicitacaoForm(request.POST or None)

    if form.is_valid():
        item = form.save(commit=False)
        item.id_solic = solicitacao

        if item.quant_itemsolic > item.id_med.estoque:
            messages.error(
                request,
                f"Não foi possível adicionar o medicamento '{item.id_med.nome_med}'. "
                f"Estoque disponível: {item.id_med.estoque}."
            )

        else:
            item.save()
            messages.success(request, "Medicamento adicionado com sucesso.")
            return redirect('adicionar_itens', solicitacao.id)

    itens = ItemSolicitacao.objects.filter(id_solic=solicitacao)

    return render(request, 'solicitacao_medicamento/itens.html', {
        'form': form,
        'itens': itens,
        'solicitacao': solicitacao
    })

def listar_solicitacoes_med(request):

    solicitacoes = SolicitacaoMedicamento.objects.all()

    return render(request, 'solicitacao_medicamento/listar.html', {
        'solicitacoes': solicitacoes
    })

def editar_solicitacao_med(request, id):

    sol = get_object_or_404(SolicitacaoMedicamento, id=id)

    if request.method == 'POST':

        novo_status = request.POST['status_solic']

        if (
            sol.status_solic != "APROVADA"
            and novo_status == "APROVADA"
        ):

            itens = ItemSolicitacao.objects.filter(id_solic=sol)

        
            for item in itens:

                if item.quant_itemsolic > item.id_med.estoque:

                    messages.error(
                        request,
                        f"Não foi possível aprovar. "
                        f"O medicamento '{item.id_med.nome_med}' possui apenas "
                        f"{item.id_med.estoque} unidade(s) em estoque."
                    )

                    return redirect(
                        'editar_solicitacao_med',
                        sol.id
                    )

            
            for item in itens:

                item.id_med.estoque -= item.quant_itemsolic
                item.id_med.save()

        sol.status_solic = novo_status
        sol.save()

        messages.success(request, "Solicitação atualizada com sucesso.")

        return redirect('listar_solicitacoes_med')

    return render(request, 'solicitacao_medicamento/editar.html', {
        'solicitacao': sol
    })

def excluir_solicitacao_med(request, id):

    sol = get_object_or_404(SolicitacaoMedicamento, id=id)

    if request.method == 'POST':
        sol.delete()
        return redirect('listar_solicitacoes_med')

    return render(request, 'solicitacao_medicamento/excluir.html', {
        'solicitacao': sol
    })